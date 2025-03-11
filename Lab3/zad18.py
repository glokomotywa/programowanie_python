def przeksztalc_temp(temp, skala_wejsciowa, skala_wyjsciowa):
    if skala_wejsciowa == "C" and skala_wyjsciowa == "F":
        return (temp * 9/5) + 32
    elif skala_wejsciowa == "F" and skala_wyjsciowa == "C":
        return (temp - 32) * 5/9
    elif skala_wejsciowa == "C" and skala_wyjsciowa == "K":
        return temp + 273.15
    elif skala_wejsciowa == "K" and skala_wyjsciowa == "C":
        return temp - 273.15
    else:
        raise ValueError("Nieobsługiwana skala")
