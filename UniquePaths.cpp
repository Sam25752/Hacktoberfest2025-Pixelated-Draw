class Solution {
public:

// int countpaths(int i, int j, int m, int n, vector<vector<int>>& dp){
//     if(i>=m || j>=n) return 0;
//     if(i==m-1 && j==n-1) return 1;
//     else return dp[i][j]= countpaths(i+1,j,m,n,dp)+countpaths(i,j+1,m,n,dp);
// }
    int uniquePaths(int m, int n) {

        // brute
        // vector<vector<int>> dp(m,vector<int>(n,-1));

        // int num=countpaths(0,0,m,n,dp);
        // if(m==1&&n==1)
        //     return num;
        // return dp[0][0];

        // optimal
        int N=m+n-2;
        int r=m-1;
        double res=1;
        for(int i=1;i<=r;i++){
            res=res*(N-r+i)/(i);
        }
        return (int)res;
    }
};
