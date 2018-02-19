if __name__ == "__main__":
    meal_cost = float(input().strip())
    tip_percent = int(input().strip())
    tax_percent = int(input().strip())
    tip_amount = meal_cost * tip_percent / 100
    tax_amount = meal_cost * tax_percent / 100
    total_cost = round(meal_cost + tip_amount + tax_amount)
    print("The total meal cost is " + str(total_cost) + " dollars.")
