
# Smart Design Score Checker

![image](https://github.com/user-attachments/assets/15790f04-0990-4438-b52b-0fbd6c583603)   ![image](https://github.com/user-attachments/assets/1e6d2682-f391-451f-8dda-c88fb9092cdf)



## Project Overview
The **Smart Design Score Checker** is an innovative tool developed for the **Adobe GenSolve Hackathon**, where it achieved recognition as a **Top 5 Percentile** project. This application leverages advanced AI to evaluate and score design assets based on key criteria such as aesthetics, usability, and alignment with design principles. Our goal is to empower designers and creators to optimize their work by providing actionable feedback and data-driven insights.

Built with a focus on efficiency and accessibility, the Smart Design Score Checker processes design files (e.g., images, UI/UX prototypes) and delivers a comprehensive score along with suggestions for improvement. This project showcases the power of AI in enhancing creative workflows, making it an invaluable tool for professionals and hobbyists alike.

## Features
- **Design Evaluation**: Analyzes design assets for visual appeal, layout balance, color harmony, and usability.
- **AI-Powered Insights**: Utilizes machine learning models to provide precise feedback and improvement suggestions.
- **User-Friendly Interface**: Built with Streamlit for an intuitive, web-based experience.
- **Comprehensive Scoring**: Generates a score out of 100 based on predefined design metrics.
- **Cross-Format Support**: Supports multiple design file formats (e.g., PNG, JPEG, Figma exports).
- **Real-Time Feedback**: Instant analysis and recommendations to streamline the design process.

## Tech Stack
- **Frontend**: Streamlit
- **Backend**: Python
- **AI/ML**: TensorFlow/PyTorch (for design analysis models)
- **File Processing**: Pillow, PyPDF2 (for image and document handling)
- **APIs**: Integration with Adobe APIs for enhanced design file compatibility
- **Environment**: Docker, Google Cloud Platform (optional for deployment)

## Installation
To set up the Smart Design Score Checker locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/RahulDasari1/Smart-Design-Score-Checker.git
   cd Smart-Design-Score-Checker
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8+ installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your API keys (e.g., Adobe API key):
   ```
   ADOBE_API_KEY=your_api_key_here
   ```

4. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
   Open your browser and navigate to `http://localhost:8501` to access the tool.

## Usage
1. **Upload Design File**: Use the web interface to upload your design file (e.g., PNG, JPEG, or PDF).
2. **Provide Context (Optional)**: Input specific design goals or criteria for tailored evaluation.
3. **Receive Score & Feedback**: The tool will analyze the file and display a score along with detailed suggestions for improvement.
4. **Iterate**: Use the feedback to refine your design and re-upload for updated scoring.

## Project Achievements
- **Top 5 Percentile** in the Adobe GenSolve Hackathon, showcasing excellence in innovation and execution.
- Recognized for seamless integration with Adobe’s ecosystem and practical application in real-world design workflows.

## Contributing
We welcome contributions from the community! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature-name`).
5. Open a Pull Request.

Please ensure your code adheres to the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- **Adobe GenSolve Hackathon** for providing an inspiring platform to innovate.
- Our team for their dedication and creativity in building this tool.
- Open-source libraries and tools that made this project possible.

## Contact
For questions, feedback, or collaboration opportunities, please reach out via GitHub Issues or contact the project lead at [dasarirahulpatel.drp@gmail.com](mailto:dasarirahulpatel.drp@gmail.com).

---
**Note**: This project is a proof-of-concept developed during a hackathon. For production use, additional optimizations and testing may be required.
