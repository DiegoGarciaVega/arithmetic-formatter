def arithmetic_arranger(problems, *boolean):
  if bool(boolean):
    calculate = True
  else:
    calculate = False

  if len(problems) > 5:
    return "Error: Too many problems."
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  for i in problems:
    op = i.split()
    if (op[1] != "+" and op[1] != "-"):
      return "Error: Operator must be '+' or '-'."
    if not (op[0].isdigit and op[2].isdigit()):
      return "Error: Numbers must only contain digits."
    if len(op[0]) >= 5 or len(op[2]) >= 5:
      return "Error: Numbers cannot be more than four digits."
    if len(op[0]) > len(op[2]):
      aux = len(op[0])
      line1 += ' '  * 2 + op[0] + ' '  * 4
      line2 += op[1] + ' ' * (len(op[0])-len(op[2])+1) + op[2] + " " * 4
      line3 += '-' * (len(op[0]) + 2) + " " * 4 
    else:
      aux = len(op[2])
      line1 += ' ' * 2 + ' ' * (len(op[2])-len(op[0])) + op[0] + ' ' * 4
      line2 += op[1] + ' ' + op[2] + ' ' * 4
      line3 += '-' * (len(op[2]) + 2) + ' ' * 4
    
    if calculate:
      if op[1] == '+':
        result = int(op[0]) + int(op[2])
      else:
       result = int(op[0]) - int(op[2])
      result = str(result)
      line4 += " " * (aux + 2 - len(result)) + result + " " * 4
  if calculate:
    arranged_problems = line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4] + '\n' + line4[:-4]
  else:
    arranged_problems = line1[:-4] + '\n' + line2[:-4] + '\n' + line3[:-4]
  return arranged_problems
