def bank(a, years, percents = 10):
    a_year = a * (years/percents)
    last_year = a + a_year
    print(last_year)
    return

bank(10000, 10)