import time
import os

def main():

    cut1  = """      
          _W_
        _ (")
         \/ /\_
          \ ;
        __///__
    """
    cut2 = """
           _   ,Nothing up my sleeve....
      _ _ (")
       M \/ /\_
          \ ;
        __///__
    """
    cut3 = """
           _   ,Nothing up my sleeve....
          (")
       _ _/_/
        M \ ;
        __///__
    """
    cut4 = """
           _   ,Nothing up my sleeve....
         _(")
        _\__/
         M\ ;
        __///__
    """
    cut5 = """
           _   ,Nothing up my sleeve....
        |\(")
       _(\__/
         M\ ;
        __///__
    """
    cut6 = """
    (\     /)
     ,\   //
      \)_(/
      /6 6;
     ( =o= )
      `)^(`
     /`   `;
    (_/   \_)
     _|   |_
    / :   ; ]
    \ :   ; / 
    /_/'-'\_\ _      ,Ta DAAAAH!
           \_(")
           _ __/
            M\ ;
           __///__
    """
    array = [cut1,cut2,cut3,cut4,cut5,cut6]
    os.system("clear")

    for i in array:
        print(i)
        time.sleep(0.5)
        os.system("clear")
    del array

if __name__ == "__main__":

    main()
