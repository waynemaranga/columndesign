def design_strength(steel_grade: int, T: float):
    """Return design strength of a section given thickness of thickest member. So far only implemented for T"""
    design_strength: int = steel_grade
    if steel_grade == 275:
        # fmt: off
        if T<16: design_strength = 275 
        elif 16<=T<40: design_strength = 265 
        elif 40<=T<63: design_strength = 255 
        elif 63<=T<80: design_strength = 245 
        elif 80<=T<100: design_strength = 235 
        elif 100<=T<150: design_strength = 225 
    elif steel_grade == 355:
        # fmt: off
        if T<16: design_strength = 355 
        elif 16<=T<40: design_strength = 345 
        elif 40<=T<63: design_strength = 335 
        elif 63<=T<80: design_strength = 325 
        elif 80<=T<100: design_strength = 315 
        elif 100<=T<150: design_strength = 295
    elif steel_grade == 460:
        # fmt: off
        if T<16: design_strength = 460
        elif 16<=T<40: design_strength = 440 
        elif 40<=T<63: design_strength = 430 
        elif 63<=T<80: design_strength = 410 
        elif 80<=T<100: design_strength = 400

    return design_strength
