import pickle
import streamlit as st


# app=Flask(__name__)
# Swagger(app)

pickle_in = open("logistic_model.pkl", "rb")
logistic_model = pickle.load(pickle_in)


# @app.route('/')
def welcome():
    return "Welcome All"


# @app.route('/predict',methods=["Get"])
def predict_note_authentication(id, loan_amnt, funded_amnt, term, int_rate, installment, emp_title, emp_length, home_ownership, annual_inc, verification_status):
    """Let's Authenticate the Banks Note
    This is using docstrings for specifications.
    ---
    parameters:
      - name: id
        in: query
        type: number
        required: true
      - name: loan_amnt
        in: query
        type: number
        required: true
      - name: funded_amnt
        in: query
        type: number
        required: true
      - name: term
        in: query
        type: number
        required: true
      - name: int_rate
        in: query
        type: number
        required: true
      - name: installment
        in: query
        type: number
        required: true
      - name: emp_title
        in: query
        type: number
        required: true
      - name: emp_length
        in: query
        type: number
        required: true
      - name: home_ownership
        in: query
        type: number
        required: true
      - name: annual_inc
        in: query
        type: number
        required: true
      - name: verification_status
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values

    """

    prediction = logistic_model.predict([[id, loan_amnt, funded_amnt, term, int_rate, installment, emp_title, emp_length, home_ownership, annual_inc, verification_status]])
    print(prediction)
    return prediction


def main():
    st.title("Loan Acceptance")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Loan Acceptance ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Id = st.text_input("id", "Type Here")
    loan_amnt = st.text_input("loan_amnt", "Type Here")
    funded_amnt = st.text_input("funded_amnt", "Type Here")
    term = st.text_input("term", "Type Here")
    int_rate = st.text_input("int_rate", "Type Here")
    installment = st.text_input("installment", "Type Here")
    emp_title = st.text_input("emp_title", "Type Here")
    emp_length = st.text_input("emp_length", "Type Here")
    home_ownership = st.text_input("home_ownership", "Type Here")
    annual_inc = st.text_input("annual_inc", "Type Here")
    verification_status = st.text_input("verification_status", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(id, loan_amnt, funded_amnt, term, int_rate, installment, emp_title, emp_length, home_ownership, annual_inc, verification_status)
    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()