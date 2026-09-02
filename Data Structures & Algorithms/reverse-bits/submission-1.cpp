class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int output = 0;
        int temp = n;
        for (size_t i = 0; i < 32; i++)
        {
            temp = n & 1;
            n = n >> 1;
            output <<= 1;
            output = output + temp;
        }
        return output;
    }
};
