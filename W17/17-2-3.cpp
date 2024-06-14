sortColors(int* nums, int numsSize) {
    fovoid r(int i=0;i<numsSize;i++){
        for(int j=i+1;j<numsSize;j++){
            if(nums[i]>nums[j]){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j]=temp;
            }
        }
    }
}