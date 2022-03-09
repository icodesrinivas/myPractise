def appendAndDelete(s, t, k):
    # Write your code here
    def common_start(s, t):
        result = []
        for i in range(len(s)):
            if i < len(t) and s[i] == t[i]:
                result.append(s[i])
            else:
                break
        return result

    remaining_s = len(s) - len(common_start(s, t))
    remaining_t = len(t) - len(common_start(s, t))
    remaining_k = k - (remaining_s + remaining_t)

    if len(s) < len(t) and k > len(t) - len(s) and remaining_k % 2 == 1:
        return 'No'

    return 'Yes' if (remaining_s + remaining_t) <= k else 'No'