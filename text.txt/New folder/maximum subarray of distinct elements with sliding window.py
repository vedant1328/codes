def maxs(nu, k):
	n = len(nu)
	i, j, ans, s = 0, 0, 0, 0
	freq = [0] * 10001
	while j < n:
		freq[nu[j]] += 1
		s += nu[j]
		if j - i + 1 == k:
			distinct = True
			for x in range(100001):
				if freq[x] > 1:
					distinct = False
					break
			if distinct:
				ans = max(ans, s)
			freq[nu[i]] -= 1
			s -= nu[i]
			i += 1
			j += 1
		else:
			j += 1
	return ans

nums = [1, 5, 4, 2, 9, 9, 9]
k = 3
print(maxs(nu, k))

