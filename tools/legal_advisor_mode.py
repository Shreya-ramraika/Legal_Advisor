def legal_advice_mode(llm, question):
    return llm.invoke(f"""
    Give step-by-step legal advice:
    {question}
    """).content