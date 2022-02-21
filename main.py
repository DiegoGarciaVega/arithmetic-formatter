# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


#print(arithmetic_arranger(['3801 - 2', '123 + 49']))
#print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
#print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
#print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
#('    3      3801      45      123\n'\n '+ 855    -    2    + 43    +  49\n'\n '-----    ------    ----    -----\n')
#('    3      3801      45      123\n'\n '+ 855    -    2    + 43    +  49\n'\n '-----    ------    ----    -----')
# Run unit tests automatically
main()
#('   32         1      45      123      988\n'\n '- 698    - 3801    + 43    +  49    +  40\n'\n '-----    ------    ----    -----    -----\n'\n ' -666     -3800      88      172     1028\n')
#('   32         1      45      123      988\n'\n '- 698    - 3801    + 43    +  49    +  40\n'\n '-----    ------    ----    -----    -----\n'\n ' -666     -3800      88      172     1028')