def expo(base, exponent):    expo.calls += 1 # Used to track recursive call count    # Write you recursive expo function here    if (exponent==0):        return 1    elif (exponent%2):        return base*expo(base, exponent-1)    else:        return (expo(base, exponent//2))**2expo.calls = 0def main():    """Tests with powers of 2."""    for exponent in range (5):        print(exponent, expo(2, exponent))if __name__ == "__main__":    main()