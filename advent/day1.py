

test_data = [1721,
             979,
             366,
             299,
             675,
             1456]

def file_to_list(filepath):
    
    values = []
    
    with open(filepath, "r") as raw_file:
        lines = raw_file.readlines()
        for line in lines:
            values.append(int(line.replace("\n", "")))
    
    return values



def find_factors_2(product, data_list):

    for num in data_list:
        for num2 in data_list:
            if num + num2 == product:
                print("first num:", num)
                print("second num:", num2)
                answer = num * num2
                print("answer is:", answer)
                return answer
            
def find_factors_3(product, data_list):
    
    for num in data_list:
        for num2 in data_list:
            for num3 in data_list:
                if num + num2 + num3 == product:
                    print("first num:", num)
                    print("second num:", num2)
                    print("third num:", num3)
                    answer = num * num2 * num3
                    print("answer is:", answer)
                    return answer

if __name__=="__main__":
    
    file1 = file_to_list("expense_report.txt")
    
    find_factors_2(2020, test_data)
    answer_pt1 = find_factors_2(2020, file1)
    answer_pt2 = find_factors_3(2020, file1)

    print("Part 1 Answer:", answer_pt1)
    print("Part 2 Answer:", answer_pt2)