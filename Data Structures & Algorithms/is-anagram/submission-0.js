class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let inputOne = s.split('').sort().join('')
        let inputTwo = t.split('').sort().join('')
        if(s.length === t.length && inputOne===inputTwo){
            return true
        }else{
            return false
        }
    }
}
