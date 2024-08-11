import numpy as np
from PIL import Image

def analyze_design(image_path):
    image = Image.open(image_path)
    score = np.random.randint(1, 100)  # Placeholder for actual AI model output
    feedback = []

    # Placeholder feedback
    if score < 50:
        feedback.append("Improve color contrast.")
        feedback.append("Consider using a larger font size.")
    else:
        feedback.append("Good design! Consider minor adjustments.")

    return score, feedback

if __name__ == "__main__":
    # Example usage
    design_score, feedback_list = analyze_design('example_design.png')
    print(f"Design Score: {design_score}")
    print("Feedback:")
    for feedback in feedback_list:
        print(f"- {feedback}")
