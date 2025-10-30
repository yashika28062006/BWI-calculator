# health_risk_cli.py
# 🩺 AI Health Risk Assessment (Command Line Version)

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)."""
    return round(weight / (height ** 2), 1)

def assess_health_risk(age, bmi, cholesterol, bp, smoker, activity):
    """Simple AI-style heuristic model for risk assessment."""
    score = 0

    # BMI risk
    if bmi < 18.5 or bmi > 30:
        score += 2
    elif bmi > 25:
        score += 1

    # Cholesterol risk
    if cholesterol == "High":
        score += 2
    elif cholesterol == "Borderline":
        score += 1

    # Blood pressure risk
    if bp == "High":
        score += 2
    elif bp == "Borderline":
        score += 1

    # Smoking
    if smoker:
        score += 2

    # Activity level
    if activity == "Low":
        score += 2
    elif activity == "Moderate":
        score += 1

    # Age
    if age > 50:
        score += 1

    # Risk classification
    if score <= 2:
        return "Low", "✅ You appear to have a **low health risk**. Keep up your healthy habits!"
    elif score <= 5:
        return "Moderate", "⚠️ Moderate risk — watch your diet and stay active."
    else:
        return "High", "🚨 High risk — consider professional medical guidance soon."

def main():
    print("🏥 AI Health Risk Assessment CLI")
    print("================================")

    try:
        # Basic Inputs
        age = int(input("Enter your age (years): "))
        gender = input("Gender (Male/Female/Other): ").strip().capitalize()
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        # Health parameters
        cholesterol = input("Cholesterol level (Normal/Borderline/High): ").strip().capitalize()
        bp = input("Blood pressure level (Normal/Borderline/High): ").strip().capitalize()
        smoker_input = input("Do you smoke regularly? (yes/no): ").strip().lower()
        smoker = smoker_input == "yes"
        activity = input("Activity level (Low/Moderate/High): ").strip().capitalize()

        # Calculate & assess
        bmi = calculate_bmi(weight, height)
        risk_level, advice = assess_health_risk(age, bmi, cholesterol, bp, smoker, activity)

        # Output summary
        print("\n==================== RESULTS ====================")
        print(f"👤 Age: {age} | Gender: {gender}")
        print(f"⚖️  BMI: {bmi}")
        print(f"📊 Health Risk Level: {risk_level}")
        print(f"💬 Advice: {advice}")
        print("=================================================")

    except ValueError:
        print("⚠️ Invalid input. Please enter numeric values for age, weight, and height.")

if __name__ == "__main__":
    main()
