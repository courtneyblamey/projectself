label lyndaending:
if imposter:
    else:
        jump 
    
    if EndCredit:
        m "I told Lynda she shouldn't doubt her knowledge."
    if EndMistake:
        "You told Lynda [EndMistake]."

label lyndareflection:
    if lynda_reflection = "instincts":
    elif lynda_reflection = "kinder":
    elif lynda_reflection = "work":
    else:
        jump reflectionend

label reflectionend

