# Simple Currency Converter
while True:
    try:
        countryNameOne = input("Enter Country Name: India,USA or Japan: ")
        countryNameTwo = input("Enter Country Name: India,USA or Japan: ")
        input1 = float(input("Enter Currency: "))
        if countryNameOne == 'India' and countryNameTwo == 'USA':
            indianUser = input1 * 0.014
            print(indianUser,'USD')
            break
        elif countryNameOne == 'USA' and countryNameTwo == 'India':
            usaUser = input1 * 73.06
            print(usaUser,'Rupees')
            break
        elif countryNameOne == 'India' and countryNameTwo == 'Japan':
            indianUser = input1 * 1.41
            print(indianUser,'Yen')
            break
        elif countryNameOne == 'Japan' and countryNameTwo == 'India':
            japaneseUser = input1 * 0.71
            print(japaneseUser,'Rupees')
            break
        elif countryNameOne == 'USA' and countryNameTwo == 'Japan':
            usaUser = input1 * 103.03
            print(usaUser,'Yen')
            break
        elif countryNameOne == 'Japan' and countryNameTwo == 'USA':
            japaneseUser = input1 * 0.0097
            print(japaneseUser,'USD')
            break
        elif countryNameOne == countryNameTwo:
            print('Please enter different country name')
        else:
            print('Country name not found')
    except ValueError:
        print('Please Enter a Number.')
    finally:
        print('Thanks For Using')


















    
        












