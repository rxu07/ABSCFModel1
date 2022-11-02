import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import numpy_financial as npf



loan_amount = 500000
payment_months = 360
interest_rate = 0.05
periodic_interest_rate = (1+interest_rate)**(1/12) - 1
monthly_installment = -1*npf.pmt(periodic_interest_rate , payment_months, loan_amount)

st.subheader("**Loan Amount:** $" + str(round(loan_amount, 2)))
st.subheader("**Monthly Installment:** $" + str(round(monthly_installment, 2)))

st.markdown("---")

st.header("**Mortgage loan Amortization**")
principal_remaining = np.zeros(payment_months)
interest_pay_arr = np.zeros(payment_months)
principal_pay_arr = np.zeros(payment_months)

for i in range(0, payment_months):

    if i == 0:
        previous_principal_remaining = loan_amount
    else:
        previous_principal_remaining = principal_remaining[i - 1]

    interest_payment = round(previous_principal_remaining * periodic_interest_rate, 2)
    principal_payment = round(monthly_installment - interest_payment, 2)

    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining

    interest_pay_arr[i] = interest_payment
    principal_pay_arr[i] = principal_payment
    principal_remaining[i] = previous_principal_remaining - principal_payment

month_num = np.arange(payment_months)
month_num = month_num + 1

principal_remaining = np.around(principal_remaining, decimals=2)

fig = make_subplots(
    rows=2, cols=1,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}]
           ]
)

fig.add_trace(
    go.Table(
        header=dict(
            values=['Month', 'Principal Payment($)', 'Interest Payment($)', 'Remaining Principal($)']
        ),
        cells=dict(
            values=[month_num, principal_pay_arr, interest_pay_arr, principal_remaining]
        )
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=month_num,
        y=principal_pay_arr,
        name="Principal Payment"
    ),
    row=2, col=1
)

fig.append_trace(
    go.Scatter(
        x=month_num,
        y=interest_pay_arr,
        name="Interest Payment"
    ),
    row=2, col=1
)

fig.update_layout(title='Mortgage Installment Payment Over Months',
                  xaxis_title='Month',
                  yaxis_title='Amount($)',
                  height=800,
                  width=1200,
                  legend=dict(
                      orientation="h",
                      yanchor='top',
                      y=0.47,
                      xanchor='left',
                      x=0.01
                  )
                  )

st.plotly_chart(fig, use_container_width=True)