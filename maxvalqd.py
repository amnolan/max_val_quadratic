def convert_to_float(input_row):
    output_row = []
    for i in input_row:
        output_row.append(float(i))
    return output_row

def find_eigenvalues(matrix):
    try:
        if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
            raise ValueError("Input matrix must be a 2x2 matrix")

        a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]

        discriminant = (a + d)**2 - 4 * (a * d - b * c)

        if discriminant >= 0:
            eigenvalue1 = (a + d + discriminant**0.5) / 2
            eigenvalue2 = (a + d - discriminant**0.5) / 2
            return eigenvalue1, eigenvalue2
        else:
            real_part = (a + d) / 2
            imaginary_part = abs(discriminant)**0.5 / 2
            eigenvalue1 = complex(real_part, imaginary_part)
            eigenvalue2 = complex(real_part, -imaginary_part)
            return eigenvalue1, eigenvalue2

    except Exception as e:
        return print("Error: ",str(e))

print("Convert matrix to quadratic form:")
print("Enter in this format comma separated")
print("Ax_1^2 + Bx_1x_2 + Cx2_^2")
print("A,B,C")
abc = convert_to_float((input()).split(","))
matrix = [[abc[0],abc[1]/2],[abc[1]/2,abc[2]]]
print("In quadratic form:")
print(matrix)
print("To find greatest val subj to constraints press enter")
input()
eigenvals = find_eigenvalues(matrix)
print("eigenvals:")
print(eigenvals)
first_eigen_prep_mtrx = []
first_eigen_prep_mtrx.append([ matrix[0][0]-eigenvals[0], matrix[0][1] ])
first_eigen_prep_mtrx.append([ matrix[1][0], matrix[1][1]-eigenvals[0] ])

second_eigen_prep_mtrx = []
second_eigen_prep_mtrx.append([ matrix[0][0]-eigenvals[1], matrix[0][1] ])
second_eigen_prep_mtrx.append([ matrix[1][0], matrix[1][1]-eigenvals[1] ])

print("eigenprep 1")
print(first_eigen_prep_mtrx)
print("eigenprep 2")
print(second_eigen_prep_mtrx)
print("Enter 1st rrefed matrix vals row by row comma sep")
top_row_first = convert_to_float((input()).split(","))
bottom_row_first = convert_to_float((input()).split(","))
print("Enter 2nd rrefed matrix vals row by row comma sep")
top_row_second = convert_to_float((input()).split(","))
bottom_row_second = convert_to_float((input()).split(","))
first = []
first.append(top_row_first)
first.append(bottom_row_first)
second = []
second.append(top_row_second)
second.append(bottom_row_second)

denom1 = top_row_first[0]*top_row_first[0] + top_row_first[1]*top_row_first[1] 

denom2 = top_row_second[0]*top_row_second[0] + top_row_second[1]*top_row_second[1] 

print("Assuming x2 is free")
print("First vector's denominator is: sqrt",denom1)
print("second vector's deoninator is: sqrt",denom2)
matrix_1 = [top_row_first[1]*-1,1]
matrix_2 = [top_row_second[1]*-1,1]
print("First unit vector (assuming) 1 for x2:")
print("[", matrix_1[0],"/ sqrt",denom1,", 1/ sqrt",denom1,"]")
print("Second unit vector (assuming) 1 for x2:")
print("[", matrix_2[0],"/ sqrt",denom2,", 1/ sqrt",denom2,"]")
