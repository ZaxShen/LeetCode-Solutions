# Last updated: 8/15/2025, 6:09:05 PM
    int sum = 0;
    for (int i = 0; i < nums.length; ++i) {
        sum += nums[i];
    }
    
    return nums.length * (nums.length + 1) / 2 - sum;
}