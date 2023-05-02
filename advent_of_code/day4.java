package advent_of_code;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

//https://adventofcode.com/2022/day/4
//sou pythonista, foi necessário muita coragem pra fazer esse exercicio em java
public class day4{
    public static void main(String[] args) {

        String inputDesafio  = lerArquivo("advent_of_code/day4.txt");
        
        String[] pares = inputDesafio.split("\n");
        //parte 1
        int soma = 0;
        String[] intervalo;
        for(String line:pares){
            intervalo = line.split(",");
            Set<Integer> strEsquerdo = numerosEmUmIntervalo(intervalo[0]);
            Set<Integer> strDireito = numerosEmUmIntervalo(intervalo[1]);
            if(strDireito.containsAll(strEsquerdo) || strEsquerdo.containsAll(strDireito)){
                soma+=1;
            }
        }
        System.out.println(soma);

        //parte 2
        soma = 0;
        for(String line:pares){
            intervalo = line.split(",");
            Set<Integer> rangeEsquerdo = numerosEmUmIntervalo(intervalo[0]);
            Set<Integer> rangeDireito =numerosEmUmIntervalo(intervalo[1]);
            Set<Integer> interseccao = new HashSet<>(rangeEsquerdo);
            interseccao.retainAll(rangeDireito);
            if(interseccao.isEmpty()==false)soma+=1;
        }
        System.out.println(soma);
    }
    /**
     * @param
     * intervalo 
     * String com o intervalo deve estar nesse formato 1-3, ou 4-7 
     * etc desde que tenha apenas 2 numeros e um hifem no meio n1-n2
     * @return Set com todos os números do intervalo 123 para 1-3 ou 4567 para 4-7 
     * como exemplo
     */
    public static Set<Integer> numerosEmUmIntervalo(String intervalo){
        String[] numeros;
        numeros = intervalo.split("-");

        int numInicial = Integer.parseInt(numeros[0]);
        int numFinal = Integer.parseInt(numeros[1])+1;

        Set<Integer> numerosDoIntervalo= new HashSet<Integer>();
        for (int i = numInicial; i < numFinal; i++) {
            numerosDoIntervalo.add(i);
        }
        return numerosDoIntervalo;
    }

    public static String lerArquivo(String diretorio){
        //copiei do chatGPT
        String nomeArquivo = diretorio;
        String texto = "";

      try {
         FileReader arquivo = new FileReader(nomeArquivo);
         BufferedReader leitor = new BufferedReader(arquivo);
         String linha = leitor.readLine();

         while (linha != null) {
            texto += linha+"\n";
            linha = leitor.readLine();
         }
         leitor.close();
         arquivo.close();

      } catch (IOException e) {
         System.out.println("Erro ao ler o arquivo: " + e.getMessage());
      }

      return texto;
    }
}
