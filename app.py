import streamlit as st
import requests

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM DESIGN
# --------------------------------------------------

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        color: #1f3c88;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 35px;
    }

    /* Form cards */
    .form-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    /* Section titles */
    .section-title {
        font-size: 22px;
        font-weight: 600;
        color: #1f3c88;
        margin-bottom: 15px;
    }

    /* Prediction result */
    .result-card {
        background-color: white;
        padding: 30px;
        border-radius: 18px;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.10);
        margin-top: 30px;
        text-align: center;
    }

    .result-title {
        font-size: 28px;
        font-weight: 700;
        color: #1f3c88;
        margin-bottom: 20px;
    }

    .result-value {
        font-size: 24px;
        font-weight: 700;
        margin: 10px 0;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        border: none;
        background-color: #1f3c88;
        color: white;
        font-size: 18px;
        font-weight: 600;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background-color: #162d66;
        color: white;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #172554;
    }

    [data-testid="stSidebar"] * {
        color: white;
    }

    /* Sidebar title */
    .sidebar-title {
        text-align: center;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 30px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        margin-top: 50px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.markdown(
    '<div class="sidebar-title">🏦 Churn AI</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown("---")

st.sidebar.markdown("### ℹ️ About")

st.sidebar.write(
    "This application predicts whether a bank customer "
    "is likely to leave the bank using an XGBoost Machine Learning model."
)

st.sidebar.markdown("---")

st.sidebar.markdown("### 🤖 Model")

st.sidebar.write("XGBoost Classifier")

st.sidebar.markdown("---")

st.sidebar.markdown("### 👨‍💻 Developer")

st.sidebar.write("Melchy BOUKOUYA")


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🏦 Bank Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Artificial Intelligence for Customer Retention'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# FORM
# --------------------------------------------------

st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

# --------------------------------------------------
# LEFT COLUMN
# --------------------------------------------------

with col1:

    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=600
    )

    geography = st.selectbox(
        "Geography",
        ["France", "Germany", "Spain"]
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    tenure = st.number_input(
        "Tenure",
        min_value=0,
        max_value=10,
        value=5
    )

    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# RIGHT COLUMN
# --------------------------------------------------

with col2:

    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    balance = st.number_input(
        "Balance",
        min_value=0.0,
        value=50000.0
    )

    num_products = st.number_input(
        "Number of Products",
        min_value=1,
        max_value=4,
        value=2
    )

    has_credit_card = st.selectbox(
        "Has Credit Card",
        [0, 1]
    )

    is_active_member = st.selectbox(
        "Is Active Member",
        [0, 1]
    )

    estimated_salary = st.number_input(
        "Estimated Salary",
        min_value=0.0,
        value=60000.0
    )

    st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

st.markdown("")

if st.button("🔮 Predict Customer Churn"):

    customer_data = {

        "credit_score": credit_score,

        "geography": geography,

        "gender": gender,

        "age": age,

        "tenure": tenure,

        "balance": balance,

        "num_products": num_products,

        "has_credit_card": has_credit_card,

        "is_active_member": is_active_member,

        "estimated_salary": estimated_salary
    }

    # --------------------------------------------------
    # API CALL
    # --------------------------------------------------

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=customer_data,
            timeout=10
        )

        if response.status_code == 200:

            result = response.json()

            prediction = result["prediction"]

            probability = result["churn_probability"]

            risk = result["risk_level"]


            # --------------------------------------------------
            # RESULT
            # --------------------------------------------------

            st.markdown(
                '<div class="result-card">',
                unsafe_allow_html=True
            )

            st.markdown(
                '<div class="result-title">📊 Prediction Result</div>',
                unsafe_allow_html=True
            )

            if prediction == 1:

                st.error(
                    "⚠️ This customer is likely to churn."
                )

            else:

                st.success(
                    "✅ This customer is unlikely to churn."
                )


            # Results columns

            result_col1, result_col2, result_col3 = st.columns(3)

            with result_col1:

                st.metric(
                    "Prediction",
                    "Churn" if prediction == 1 else "No Churn"
                )

            with result_col2:

                st.metric(
                    "Churn Probability",
                    f"{probability * 100:.2f}%"
                )

            with result_col3:

                st.metric(
                    "Risk Level",
                    risk
                )


            st.markdown('</div>', unsafe_allow_html=True)


        else:

            st.error(
                f"API Error: {response.status_code}"
            )


    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Unable to connect to the FastAPI server. "
            "Make sure the API is running on port 8000."
        )


    except requests.exceptions.Timeout:

        st.error(
            "⏱️ The API request took too long. "
            "Please try again."
        )


    except Exception as e:

        st.error(
            f"Unexpected error: {e}"
        )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    '<div class="footer">'
    'Bank Customer Churn Prediction System • '
    'Powered by XGBoost & FastAPI'
    '</div>',
    unsafe_allow_html=True
)