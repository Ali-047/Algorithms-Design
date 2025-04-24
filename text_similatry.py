import tkinter as tk
import hashlib
import difflib

# Bloom Filter implementation
class BloomFilter:
    def __init__(self, size, hash_count):
        try:
            if not isinstance(size, int) or not isinstance(hash_count, int):
                raise TypeError("Size and hash_count must be integers")
            if size <= 0 or hash_count <= 0:
                raise ValueError("Size and hash_count must be positive")
            self.size = size
            self.hash_count = hash_count
            self.bit_array = [0] * size
        except (TypeError, ValueError) as e:
            raise e

    def _hash(self, item, seed):
        try:
            hash_obj = hashlib.md5((str(item) + str(seed)).encode('utf-8'))
            hash_digest = hash_obj.hexdigest()
            return int(hash_digest, 16) % self.size
        except Exception as e:
            raise ValueError(f"Error in hashing: {str(e)}")
    
    def add(self, item):
        try:
            for seed in range(self.hash_count):
                self.bit_array[self._hash(item, seed)] = 1
        except Exception as e:
            raise ValueError(f"Error adding item to Bloom filter: {str(e)}")
            
    def check(self, item):
        try:
            for seed in range(self.hash_count):
                if self.bit_array[self._hash(item, seed)] == 0:
                    return False
            return True
        except Exception as e:
            raise ValueError(f"Error checking item in Bloom filter: {str(e)}")

# Main GUI Application class using Tkinter
class MainApp:
    def __init__(self, master):
        try:
            self.master = master
            master.title("Text Similarity Analyzer")
            master.geometry("600x600")
            self.bloom_filter = BloomFilter(size=1000, hash_count=3)
            
            # Label and text widget for the first text
            self.label1 = tk.Label(master, text="Enter First Text")
            self.label1.pack(pady=5)
            self.text1 = tk.Text(master, height=8, width=70)
            self.text1.pack(pady=5)
            
            # Label and text widget for the second text
            self.label2 = tk.Label(master, text="Enter Second Text")
            self.label2.pack(pady=5)
            self.text2 = tk.Text(master, height=8, width=70)
            self.text2.pack(pady=5)
            
            # Button to trigger analysis
            self.compare_button = tk.Button(master, text="Analyze Similarity", command=self.analyze_texts)
            self.compare_button.pack(pady=10)
            
            # Label to display the result and explanation
            self.result_label = tk.Label(master, text="", justify="left", wraplength=500)
            self.result_label.pack(pady=10)
            
        except Exception as e:
            raise ValueError(f"Error initializing GUI: {str(e)}")
    
    def analyze_texts(self):
        try:
            # Get text from both input fields
            text1 = self.text1.get("1.0", tk.END).strip()
            text2 = self.text2.get("1.0", tk.END).strip()
            
            # Enhanced empty input validation
            if not text1 and not text2:
                self.result_label.config(text="Error: Both text boxes are empty. Please enter text to compare.", fg="red")
                return
            elif not text1:
                self.result_label.config(text="Error: First text box is empty. Please enter text to compare.", fg="red")
                return
            elif not text2:
                self.result_label.config(text="Error: Second text box is empty. Please enter text to compare.", fg="red")
                return
            
            # Reset text color for normal results
            self.result_label.config(fg="black")
            
            # Add words to Bloom filter and check overlap
            words1 = text1.lower().split()
            words2 = text2.lower().split()
            
            for word in words1:
                self.bloom_filter.add(word)
            
            bloom_matches = sum(1 for word in words2 if self.bloom_filter.check(word))
            bloom_similarity = bloom_matches / len(words2) if words2 else 0
            
            # Calculate Jaccard similarity
            jaccard_score = jaccard_similarity(words1, words2)
            
            # Calculate normalized Levenshtein distance
            lev_distance = levenshtein_distance(text1.lower(), text2.lower())
            max_len = max(len(text1), len(text2))
            lev_similarity = 1 - (lev_distance / max_len if max_len > 0 else 0)
            
            # Find common sequences
            common_seqs = get_common_sequences(text1, text2, min_len=3)
            
            # Calculate overall similarity score (weighted average)
            similarity_score = (bloom_similarity * 0.3 + jaccard_score * 0.4 + lev_similarity * 0.3) * 100
            
            # Generate explanation
            explanation = f"Similarity: {similarity_score:.1f}%\n\nAnalysis:\n"
            if common_seqs:
                explanation += "\nCommon phrases found:\n- " + "\n- ".join(common_seqs)
            
            if similarity_score > 80:
                explanation += "\n\nHigh similarity detected! The texts are very similar."
            elif similarity_score > 50:
                explanation += "\n\nModerate similarity detected. The texts share some common elements."
            else:
                explanation += "\n\nLow similarity detected. The texts are mostly different."
            
            self.result_label.config(text=explanation)
            
        except Exception as e:
            self.result_label.config(text=f"Error analyzing texts: {str(e)}")

# Standalone functions
def jaccard_similarity(set1, set2):
    try:
        if not isinstance(set1, (set, list, tuple)) or not isinstance(set2, (set, list, tuple)):
            raise TypeError("Inputs must be sets, lists, or tuples")
        set1, set2 = set(set1), set(set2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        if union == 0:
            return 0
        return intersection / union
    except TypeError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error calculating Jaccard similarity: {str(e)}")

def levenshtein_distance(s1, s2):
    try:
        if not isinstance(s1, str) or not isinstance(s2, str):
            raise TypeError("Inputs must be strings")
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

        return dp[m][n]
    except TypeError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error calculating Levenshtein distance: {str(e)}")
    

def get_common_sequences(s1, s2, min_len=2):
    try:
        if not isinstance(s1, str) or not isinstance(s2, str):
            raise TypeError("Inputs must be strings")
        if not isinstance(min_len, int) or min_len < 1:
            raise ValueError("min_len must be a positive integer")
            
        matcher = difflib.SequenceMatcher(None, s1, s2)
        blocks = matcher.get_matching_blocks()[:-1]
        common = []
        for block in blocks:
            if block.size >= min_len:
                substring = s1[block.a: block.a + block.size]
                if substring not in common:
                    common.append(substring)
        return common
    except (TypeError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error finding common sequences: {str(e)}")
    
def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()