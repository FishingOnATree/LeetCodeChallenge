import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

/*
 * https://leetcode.com/problems/design-twitter/
 * beats 97% :)
 */

public class Twitter {
	private Map<Integer,  Set<Integer>> followership;
	private Map<Integer, List<Tweet>> userTweetMap;

    /** Initialize your data structure here. */
    public Twitter() {
    	followership = new HashMap<Integer, Set<Integer>>();
    	userTweetMap = new HashMap<Integer, List<Tweet>>();
    }

    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
    	List<Tweet> tweetList = userTweetMap.get(userId);
    	if (tweetList == null) {
    		tweetList = new ArrayList<Tweet>();
    		userTweetMap.put(userId, tweetList);
    	}
    	tweetList.add(new Tweet(tweetId));
    }

    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    public List<Integer> getNewsFeed(int userId) {
    	List<Integer> tweetList = new ArrayList<Integer>();
    	Set<Integer> followeeSet = followership.get(userId);
    	if (followeeSet == null) {
    		followeeSet = new HashSet<Integer>();
    	} else {
    		followeeSet = new HashSet<Integer>(followeeSet);
    	}
    	followeeSet.add(userId);
    	// get all tweets
    	List<Integer> indexTracker = new ArrayList<Integer>();
    	List<List<Tweet>> tweetTracker = new ArrayList<List<Tweet>>();
    	for (Integer followee: followeeSet) {
    		List<Tweet> tweets = userTweetMap.get(followee);
    		if (tweets != null && !tweets.isEmpty()) {
    			indexTracker.add(tweets.size() - 1);
    			tweetTracker.add(tweets);
    		}
    	}
    	// backtracking
    	for (int i=1; i<=10 && !tweetTracker.isEmpty(); i++) {
    		int selectedUserIndex = -1;
    		int selectedTweetIndex = -1;
    		for (int j=0; j<indexTracker.size(); j++) {
    			if (selectedUserIndex == -1 ||
    					tweetTracker.get(j).get(indexTracker.get(j)).getTime()
    					> tweetTracker.get(selectedUserIndex).get(selectedTweetIndex).getTime()) {
    				selectedUserIndex = j;
    				selectedTweetIndex = indexTracker.get(j);
    			}
    		}
    		if (selectedUserIndex == -1) {
    			break;
    		} else {
    			tweetList.add(tweetTracker.get(selectedUserIndex).get(selectedTweetIndex).getTweetId());
    			int newTweetPos = indexTracker.remove(selectedUserIndex) - 1;
    			if (newTweetPos < 0) {
    				tweetTracker.remove(selectedUserIndex);
    			} else {
    				indexTracker.add(selectedUserIndex, newTweetPos);
    			}
    		}
    	}
    	return tweetList;
    }

    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
    	Set<Integer> followingSet = followership.get(followerId);
    	if (followingSet == null) {
    		followingSet = new HashSet<Integer>();
    		followership.put(followerId, followingSet);
    	}
    	followingSet.add(followeeId);
    }

    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
    	Set<Integer> followingSet = followership.get(followerId);
    	if (followingSet != null) {
        	followingSet.remove(followeeId);
    	}
    }

    public static void main(String[] args) {
    	Twitter a = new Twitter();
    	a.postTweet(1, 4);
    	a.postTweet(2, 5);
    	a.unfollow(1, 2);
    	a.follow(1, 2);
    	System.out.println(a.getNewsFeed(1));
    }
}

class Tweet{
	private static int time_count = 0;
	int tweetId;
	long time;

	public Tweet(int tweetId) {
		super();
		this.tweetId = tweetId;
		this.time = assignTime();
	}

	private synchronized int assignTime() {
		return time_count++;
	}

	public int getTweetId() {
		return tweetId;
	}
	public long getTime() {
		return time;
	}
}


/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */