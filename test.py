from Utilities import *

def main():
    testRandom(20, 20, 20, 100)


def testRandom(size, max_x, max_y, cases):
    print("\n\t========\n")

    lenght_passed = 0
    duplicate_passed = 0

    for i in range(cases):
        test = getMines(size, max_x, max_y)
        if len(test) == size:
            print("Lenght test pased!")
            lenght_passed += 1

        has_duplicates = False
        for i in test:
            counter = 0
            for j in test:
                if str(i) == str(j):
                    if counter == 0:
                        counter += 1
                    else:
                        print(f"Duplicate found: {i}")
                        has_duplicates = True
        
        if not has_duplicates:
            print("Duplicates test passed!")
            duplicate_passed += 1

        print("\n\t========\n")

    print(f"Lenght test passed: {lenght_passed}/{cases}")
    print(f"Duplicate test passed: {duplicate_passed}/{cases}")
        

if __name__ == "__main__":
    main()

