package palindromo;

import java.util.ArrayList;

public class Palindromo {

    public static void main(String[] args) {
        int digito1=0;
        int digito2=0;
        int digito3=0;
        int digito4=0;
        
       ArrayList<String> datos= new ArrayList<>();
        
        for(int p=0; p<2;p++){
            for(int k=0; k<10;k++){
                for(int j=0;j<6;j++){
                    for(int i=0; i<10;i++){
      
                          datos.add(digito1+""+digito2+":"+digito3+digito4+"\n");
                            digito4++;
                    }
                digito4=0;
                digito3++;
       
                }
        digito3=0;
        digito2++;
            }
           digito2=0;
           digito1++;
    }
        
            if(digito1==2){
           for(int k=0; k<4;k++){
                for(int j=0;j<6;j++){
                    for(int i=0; i<10;i++){
     
                          datos.add(digito1+""+digito2+":"+digito3+digito4+"\n");
                            digito4++;
                    }
                digito4=0;
                digito3++;
       
                }
        digito3=0;
        digito2++;
            }
            }
            
           
           int conta=datos.size();
           System.out.println("Palindromos: \n");
           for(int q=0; q<conta; q++){
              String aux=datos.get(q);
               
              if(aux.charAt(0)==aux.charAt(4) && aux.charAt(1)== aux.charAt(3)){
                System.out.println(datos.get(q));
              }
              
           }
        }
    
   }