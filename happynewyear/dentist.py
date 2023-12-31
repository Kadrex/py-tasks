"""Your biggest nightmare is about to come True - you're going to the dentist!"""


def take_maximum(gov_exp_leftover: float, health_insurance_percentage: int, health_insurance_max_exp: float) -> tuple:
    """
    Given the information you are given, calculate the maximum bill so that you use as much insurance money as possible,
    but as little your money as possible. Also, calculate how much you have to pay. Return tuple of these two values,
    in that same order.
    Float values must not have more than two decimal points.

    Rules:
    * You can use as much gov_exp_leftover as you like. This value is guaranteed to be >= 0.
    * Government will only cover up to half of the total expense.
    * The health insurance covers health_insurance_percentage percentage of the cost that you personally paid,
    but no more than health_insurance_max_exp.
    * It is guaranteed that 0 <= health_insurance_percentage <= 100
    * It is guaranteed that health_insurance_max_exp >= 0.

    Example:
    gov_exp_leftover = 40
    health_insurance_percentage = 80
    health_insurance_max_exp = 300
    Result: (415, 75)

    :param gov_exp_leftover:
    :param health_insurance_percentage:
    :param health_insurance_max_exp:
    :return:
    """
    pass
