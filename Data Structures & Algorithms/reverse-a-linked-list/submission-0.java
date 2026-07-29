/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode dummy = new ListNode();
        ListNode curr = dummy;
        List<Integer> arr = new ArrayList<>();
        while(head!= null){
            arr.add(head.val);
            head=head.next;
        }
        for (int i=arr.size()-1 ; i>=0 ; i--){
            curr.next = new ListNode(arr.get(i));
            curr = curr.next;
        }
        return dummy.next;
    }
}
