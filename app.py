import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import cv2
import time

# Page config
st.set_page_config(
    page_title="🏥 AI Healthcare Assistant",
    page_icon="🏥",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(90deg, #0ea5e9 0%, #06b6d4 100%);
    padding: 2rem;
    border-radius: 10px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}
.feature-card {
    background: #f8fafc;
    padding: 1.5rem;
    border-radius: 10px;
    border-left: 4px solid #0ea5e9;
    margin: 1rem 0;
}
</style>
""", unsafe_allow_html=True)

def get_chatbot_response(user_input):
    user_input = user_input.lower()
    if "fever" in user_input or "बुखार" in user_input:
        return "बुखार के लिए कृपया तापमान और दिन बताएँ।"
    elif "headache" in user_input or "सिर दर्द" in user_input:
        return "सिर दर्द के लिए आराम करें और पानी पिएं।"
    elif "cough" in user_input or "खांसी" in user_input:
        return "खांसी के लिए गर्म पानी से गरारे करें और शहद लें।"
    elif "chest pain" in user_input or "छाती में दर्द" in user_input:
        return "छाती में दर्द गंभीर लक्षण हो सकता है, तुरंत अस्पताल जाएं।"
    else:
        return "कृपया अपने लक्षण विस्तार से बताएं। मैं मदद करूंगा।"

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏥 AI Healthcare Assistant</h1>
        <p>X-ray Analysis | Voice Reports | AI Chatbot | 3D Visualization | AR/VR</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar navigation
    st.sidebar.title("🩺 Navigation")
    page = st.sidebar.selectbox(
        "Select Module",
        ["🏠 Dashboard", "🔬 X-ray Analysis", "🎤 Voice Reports", 
         "💬 AI Chatbot", "🧊 3D Reconstruction", "🥽 AR/VR Support"]
    )
    
    if page == "🏠 Dashboard":
        show_dashboard()
    elif page == "🔬 X-ray Analysis":
        show_xray_analysis()
    elif page == "🎤 Voice Reports":
        show_voice_reports()
    elif page == "💬 AI Chatbot":
        show_ai_chatbot()
    elif page == "🧊 3D Reconstruction":
        show_3d_reconstruction()
    elif page == "🥽 AR/VR Support":
        show_ar_vr_support()

def show_dashboard():
    st.header("Healthcare AI Dashboard")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("X-rays Analyzed", "157", "↗ 12%")
    with col2:
        st.metric("Voice Reports", "89", "↗ 8%")
    with col3:
        st.metric("AI Consultations", "234", "↗ 15%")
    with col4:
        st.metric("3D Models", "45", "↗ 5%")

def show_xray_analysis():
    st.header("🔬 AI X-ray Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Upload X-ray Image")
        uploaded_file = st.file_uploader(
            "Choose X-ray file", 
            type=['png', 'jpg', 'jpeg']
        )
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded X-ray")
            
            if st.button("🔍 Analyze X-ray", type="primary"):
                with st.spinner("AI analyzing..."):
                    time.sleep(3)  # Simulate analysis
                st.success("Analysis Complete!")
                
                # Show results
                st.session_state.analysis_result = {
                    "condition": "Pneumonia",
                    "confidence": 0.94,
                    "findings": ["Right lower lobe consolidation", "Inflammatory infiltrates"],
                    "recommendations": "Antibiotic therapy recommended"
                }
    
    with col2:
        st.subheader("Analysis Results")
        if hasattr(st.session_state, 'analysis_result'):
            result = st.session_state.analysis_result
            st.success(f"✅ Condition: {result['condition']}")
            st.info(f"🎯 Confidence: {result['confidence']:.0%}")
            
            st.markdown("**Findings:**")
            for finding in result['findings']:
                st.write(f"• {finding}")
            
            st.markdown("**Recommendations:**")
            st.write(result['recommendations'])

def show_voice_reports():
    st.header("🎤 Voice-Based Report Generation")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Voice Input")
        language = st.selectbox("Language", ["English", "Hindi", "Hinglish"])
        
        if st.button("🔴 Start Recording", type="primary"):
            with st.spinner("Recording..."):
                time.sleep(3)
            st.success("Recording Complete!")
            
            # Simulate transcription
            sample_text = "Patient presents with chest pain and shortness of breath. Physical examination shows decreased breath sounds."
            st.session_state.transcription = sample_text
    
    with col2:
        st.subheader("Generated Report")
        if hasattr(st.session_state, 'transcription'):
            st.text_area("Transcription", st.session_state.transcription, height=200)
            
            if st.button("📄 Generate Report"):
                st.download_button(
                    "📥 Download Report",
                    st.session_state.transcription,
                    "medical_report.txt"
                )

def show_ai_chatbot():
    st.header("💬 AI Doctor-Patient Chatbot")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "नमस्ते! मैं आपका AI डॉक्टर हूँ। कैसे मदद कर सकता हूँ?"}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("अपने symptoms बताएं..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_chatbot_response(prompt)

        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"):
            st.markdown(response)

def show_3d_reconstruction():
    st.header("🧊 3D X-ray Reconstruction")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Settings")
        resolution = st.slider("Resolution", 64, 512, 256)
        opacity = st.slider("Opacity", 0.3, 1.0, 0.7)
        
        if st.button("🚀 Generate 3D Model"):
            with st.spinner("Creating 3D model..."):
                time.sleep(5)
            st.success("3D Model Generated!")
            st.session_state.model_3d = True
    
    with col2:
        st.subheader("3D Visualization")
        if hasattr(st.session_state, 'model_3d'):
            fig = go.Figure(data=go.Scatter3d(
                x=[1, 2, 3, 4],
                y=[10, 11, 12, 13],
                z=[2, 3, 4, 5],
                mode='markers'
            ))
            fig.update_layout(title="3D Chest Cavity Model")
            st.plotly_chart(fig)

def show_ar_vr_support():
    st.header("🥽 AR/VR Medical Applications")
    
    tab1, tab2 = st.tabs(["🔍 AR X-ray Overlay", "🎮 VR Training"])
    
    with tab1:
        st.subheader("Augmented Reality Features")
        st.info("📱 AR X-ray overlay functionality")
        
        if st.button("📱 Start AR Session"):
            st.success("🚀 AR session activated!")
    
    with tab2:
        st.subheader("Virtual Reality Training")
        training_module = st.selectbox(
            "Training Module",
            ["Basic Anatomy", "Surgical Procedures", "Emergency Response"]
        )
        
        if st.button("🎮 Launch VR Training"):
            st.success("🥽 VR training started!")

if __name__ == "__main__":
    main()
