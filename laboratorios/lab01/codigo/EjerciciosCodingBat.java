/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package Laboratorio1;

/**
 *
 * @author User
 */
public class Main {
    public static void main(String[] args) {
        
    }
    //EJERCICIOS DE CODING BAT.JAVA RECURSION 1
    public int count7(int n) {
        if(n ==0){//c1=2
          return 0;//c2=1
        }
        else{
          if(n%10==7){//c3=3
            return 1+count7(n/10);//T(n)=c4+tT(n/10)
          }
          else{
            return count7(n/10);//T(n)=c5+T(n/10)
          }
        }
      }
    //con el peor caso resuelvo la ecuacion y seria igual a: T(n)=C4log10(n)+c1
    public int bunnyEars(int bunnies) {
        if(bunnies==0){//c1=2
          return 0;//c2=1
        }
        else{
          return 2+bunnyEars(bunnies-1);//T(n)=c3n+c1
        }   
    }
    //con el peor caso seria: T(n)=
    public int fibonacci(int n) {
        if(n==2||n==1){//c1=4
          return 1;//c2=1
        }
        else{
          return fibonacci(n-1)+fibonacci(n-2);//T(n)=c3+(n-1)+(n-2)
    }}
    //en el peor caso seria: T(n)= -C3+C1Fn+C2Ln
    /**
     *
     * @param bunnies
     * @return
     */
    public int bunnyEars2(int bunnies) {
        if(bunnies ==0){//c1=2
          return 0;//c2=1
        }
        else{
          if(bunnies%2==0){//c3=3
            return 3+bunnyEars2(bunnies-1);//T(n)=c4+t(n-1)
          }
          else{
            return 2+bunnyEars2(bunnies-1);//T(n)=c5+t(n-1)
          }
        }
        }
        //en el peor de los casos seria: T(n)=c5n+c1
    public int triangle(int rows) {
        if(rows==0){//c1=2
          return 0;//c2=1
        }
        else{
          return rows + triangle(rows-1);//T(n)=c3+t(n-1)
        }
    }
    //en el peor de los casos seria: T(n)=c3n+C1
    public int sumDigits(int n) {
        if(n<1){//c1=2
          return 0;//c2=1
        }
        else{
          return n%10+sumDigits(n/10);//T(n)=c3+t(n/10)
        }
    }
    //en el peor de los casos seria: T(n)=c3Log10(n)+c1

    //ejercicios codingbat recursion 2
 
    public boolean split53(int[] nums) {
        return aux(nums, 0, 0, 0);
     }


      private boolean aux ( int[] nums, int index, int S1, int S2 ) {
        if ( index >= nums.length ) {//C1=2
          return S1 == S2;//C2=2
        }

        int value = nums[index];//C3=1

        if (value%5 == 0)//C4=3
          return aux(nums, index + 1, S1 + value, S2);//T(n)=t(n+1)+c5 (n=index)
        else if (value%3 == 0)//c6=3
          return aux(nums, index + 1, S1, S2 + value);//T(n)=t(n+1)+c7
        else     
          return (aux(nums, index + 1, S1 + value, S2) || 
            aux(nums, index + 1, S1, S2 + value));//T(n)=t(n+1)+c8
      }//peor caso: T(n)=t(n+1)+c8
      //WOLFRAM: T(n) = c_1 - c^8 n (where c_1 is an arbitrary parameter)

   
    public boolean groupSum6(int start, int[] nums, int target) {
        if (start >= nums.length){//c1=3
            return target == 0;//c2=2
        }
        if (nums[start] == 6){//c3=3
            return groupSum6(start + 1, nums, target - nums[start]);}//T(n)=t(n+1)+c4
        return groupSum6(start + 1, nums, target - nums[start])//T(n)=t(n+1)+c5
                || groupSum6(start + 1, nums, target);
    }
    //peor caso: T(n)=t(n+1)+c5
    //EN WOLFRAM: T(n)=c1-c5n
    public boolean groupSum5(int start, int[] nums, int target) {
        if (start >= nums.length){//c1=2
            return target == 0;}//c2=1
        if (nums[start] == 5)//c3=2
            {return groupSum5(start + 1, nums, target - nums[start]);}//T(n)=t(n+1)+c4
            if(start+1==nums.length-1){//c5=3
            if(nums[start+1]==1){//c6=3
              return groupSum5(start+1,nums,target);//T(n)=t(n+1)+c7
            }}
            //peor caso: T(n)=t(n+1)+c5
    //EN WOLFRAM: T(n)=c1-c5n
        return groupSum5(start + 1, nums, target - nums[start])
                || groupSum5(start + 1, nums, target);
    }
    public boolean groupNoAdj(int start, int[] nums, int target) {
    if (start >= nums.length){//c1=2
                    return target == 0;  //c3=2  
     }
    else{
        boolean anormal = groupNoAdj(start+2, nums, target - nums[start]);//T(n)=c4+t(n+2)
        boolean normal = groupNoAdj(start+1, nums, target);//T(n)=c5+t(n+1)
        return anormal || normal;//c6=2
      
    }
}
    public boolean SplitArray(nums){
        return auxsplit(0,0,0,nums);
    }
    public boolean auxsplit(int start,int num1,int num2,int[] nums){
        if(start >=nums.length){//c1=2
            return num1==num2;//c2=2
        }
        else{
            return auxsplit(start+1,num1+nums[start],num2,nums) || auxsplit(start+1,num1,num2+nums[start],nums);//T(n)=t(n+1)+c3
        }
    }
}




