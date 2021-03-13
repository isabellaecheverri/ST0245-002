/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Lab2;

/**
 *
 * @author User
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
    }
    //EJERCICIOS CODINGBAT ARRAY 2
    public int countEvens(int[] nums) {
        int contador=0;
        for(int i=0;i<nums.length;i++){
          if(nums[i]%2==0){
            contador = contador+1;
          }
          else{
            contador=contador;
          }
        }
        return contador;
    }
    public int bigDiff(int[] nums) {
        int max =0;
        int min=5000;
        for(int i=0;i<nums.length;i++){
          if(nums[i]>max){
            max = nums[i];
          }
          if(nums[i]<min){
            min = nums[i];
          }
        }
        return max-min;
    }
    public int centeredAverage(int[] nums) {
	int min = nums[0];
	int max = nums[0];
	int suma = nums[0];
	for(int i = 1; i < nums.length; i++)
	{
		suma  =suma+ nums[i];
		if(nums[i] > max)
			max = nums[i];
		else if(nums[i] < min)
			min = nums[i];
	}
	return (suma-max-min) / (nums.length - 2);
    }
    public int sum13(int[] nums) {
            int suma= 0;
            for(int i=0;i<nums.length;i++){

              if(nums.length==0){
                return 0;
              }
              suma = suma+nums[i];
              if(nums[i]==13){
                i=i+1;
                suma = suma-13;
              }
            }
            return suma;
        }
    public int sum67(int[] nums) {
        int suma = 0;
        int index = 0;
        for(int i=0;i<nums.length;i++){
          suma = suma+nums[i];
          if(nums[i]==6){
            suma = suma -6;
            for(int j=i;j<nums.length;j++){
              if(nums[j]==7){
                index = j;
                i=j;
              }
            }
          }
        }
        return suma;
    }
    //ARRAY3
    @SuppressWarnings("empty-statement")
    public int maxSpan(int[] nums) {
        int var1 = 0;
        int span =0;
        int j;
        if(nums.length==1){
            return 1;
        }
        if(nums.length==0){
          return 0;
        }
            for(int i = 0; i < nums.length; i++)
                    {
                            for(j = nums.length - 1; nums[i] != nums[j]; j--);
                            var1 = (j - i)+1;
                            if(var1 > span){
                                    span = var1;
                            }
                    }
              return span;
      }
        public boolean canBalance(int[] nums){
            return auxsplit(0,0,0,nums);
          }
          public boolean auxsplit(int start,int num1,int num2,int[] nums){
            if(start >=nums.length){//c1=2
              return num1==num2;
            }
            else{
             return auxsplit(start+1,num1+nums[start],num2,nums) || auxsplit(start+1,num1,num2+nums[start],nums);//T(n)=t(n+1)+c3
           }
        }
          
        public boolean linearIn(int[] outer, int[] inner) {
                int cont =0;
                for(int i =0;i<inner.length;i++){
                  for(int j =0;j<outer.length;j++){
                    if(inner[i]==outer[j]){
                      cont = cont +1;
                      break;
                    }
                  }
                }
                return cont>=inner.length;
              }
        public int[] seriesUp(int n) {
            int[] seriesUp = new int[(n*(n+1))/2];
            int count = 0;
            for(int i = 1; i<= n; i++){
              int it = n-i;
              for(int j = 1; j<= n - it; j++){
                seriesUp[count] = j;
                count++;
              }
            }
            return seriesUp;
          }
        public int countClumps(int[] nums) {
        int ocurr = 0;
        int rep = 0;
        for(int j = 0;j<nums.length-1;j++){
          if(nums[j] == nums[nums.length-1] && nums[j] == nums[j+1] && rep == 1){
            ocurr = 1;
          }
          if(nums[j] == nums[j+1] && rep == 0){
            rep++;
          }else{
            rep = 0;
          }
          if(rep == 1){
            ocurr++;
          }
        } 
        return ocurr;
        }
        

}
