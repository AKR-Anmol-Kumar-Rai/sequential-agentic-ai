import streamlit as st

from agents.research_agent import research_agent
from agents.planning_agent import planning_agent
from agents.coding_agent import coding_agent
from agents.debugging_agent import debugging_agent
from agents.docs_agent import docs_agent
from tools.execute_tools import run_code


# Page config
st.set_page_config(
    page_title="Sequential Chaining AI",
    page_icon="🤖",
    layout="wide"
)


# Custom CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to right, #0f172a, #1e293b);
        color: white;
    }

    .main-title {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        color: white;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #cbd5e1;
        margin-bottom: 40px;
    }

    .section-title {
        color: white;
        font-size: 28px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    .box {
        background-color: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 20px;
        border: 1px solid rgba(255,255,255,0.08);
    }

    /* Generate Button */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 55px;
        font-size: 18px;
        font-weight: bold;
        background: linear-gradient(to right, #3b82f6, #9333ea);
        color: white;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background: linear-gradient(to right, #06b6d4, #2563eb);
        transform: scale(1.03);
        box-shadow: 0px 0px 20px rgba(59,130,246,0.5);
    }

    /* Download Buttons */
    .stDownloadButton>button {
        width: 100%;
        border-radius: 12px;
        height: 50px;
        font-size: 16px;
        font-weight: bold;
        background: linear-gradient(to right, #10b981, #059669);
        color: white;
        border: none;
        transition: all 0.3s ease;
    }

    .stDownloadButton>button:hover {
        background: linear-gradient(to right, #22c55e, #16a34a);
        transform: scale(1.03);
        box-shadow: 0px 0px 20px rgba(34,197,94,0.5);
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<div class="main-title">Sequential Chaining Agentic AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Research → Plan → Code → Debug → Document</div>',
    unsafe_allow_html=True
)


# Input Section
st.markdown(
    '<div class="section-title">Project Idea</div>',
    unsafe_allow_html=True
)

query = st.text_input(
    "Enter your project idea and press Enter..."
)

generate_clicked = st.button("Generate Project 🚀")


# Auto trigger on Enter OR button click
if query or generate_clicked:

    if query.strip():

        # Research Agent
        with st.spinner("Researching..."):
            research_output = research_agent.run(query)

        st.markdown(
            '<div class="section-title">Research Agent</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="box">{research_output.content}</div>',
            unsafe_allow_html=True
        )

        # Planning Agent
        with st.spinner("Planning..."):
            planning_output = planning_agent.run(
                research_output.content
            )

        st.markdown(
            '<div class="section-title">Planning Agent</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="box">{planning_output.content}</div>',
            unsafe_allow_html=True
        )

        # Coding Agent
        with st.spinner("Generating Code..."):
            coding_output = coding_agent.run(
                planning_output.content
            )

        # Clean markdown if model adds it
        clean_code = (
            coding_output.content
            .replace("```python", "")
            .replace("```", "")
        )

        st.markdown(
            '<div class="section-title">Coding Agent</div>',
            unsafe_allow_html=True
        )
        st.code(clean_code, language="python")

        # Execute Code directly
        with st.spinner("Executing Code..."):
            execution_result = run_code(clean_code)

        st.markdown(
            '<div class="section-title">Execution Result</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="box">{execution_result}</div>',
            unsafe_allow_html=True
        )

        # If error found → Debugging Agent
        if "Traceback" in execution_result or "Error" in execution_result:

            with st.spinner("Fixing Errors..."):
                debugging_output = debugging_agent.run(
                    f"""
                    Here is the generated code:

                    {clean_code}

                    Here is the error:

                    {execution_result}

                    Fix the code and return ONLY corrected raw Python code.
                    """
                )

            fixed_code = (
                debugging_output.content
                .replace("```python", "")
                .replace("```", "")
            )

            st.markdown(
                '<div class="section-title">Debugging Agent Fix</div>',
                unsafe_allow_html=True
            )
            st.code(fixed_code, language="python")

            st.download_button(
                label="Download Fixed train.py",
                data=fixed_code,
                file_name="train_fixed.py",
                mime="text/plain"
            )

        else:
            st.success(
                "Code executed successfully. No debugging needed."
            )

        # Documentation Agent
        with st.spinner("Generating Documentation..."):
            docs_output = docs_agent.run(planning_output.content)

        st.markdown(
            '<div class="section-title">Documentation Agent</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            f'<div class="box">{docs_output.content}</div>',
            unsafe_allow_html=True
        )

        # Download Section
        st.markdown(
            '<div class="section-title">Download Files</div>',
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2, gap="large")

        with col1:
            st.download_button(
                label="📄 Download train.py",
                data=clean_code,
                file_name="train.py",
                mime="text/plain"
            )

        with col2:
            st.download_button(
                label="📘 Download README.md",
                data=docs_output.content,
                file_name="README.md",
                mime="text/markdown"
            )
    else:
        st.warning("Please enter a project idea.")


#  there was a pronlem in debugging because when huge codeis given to the run_code(code)
# the tool it fails to compute because agent is passing the entire huge generated code inside the tool call.Groq often fails when tool arguments are too large.That’s why it crashes.

# so we used idea that if the code fails then we will use run_code as a function not a tools so it will not fail