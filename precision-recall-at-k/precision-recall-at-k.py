def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Slice the recommendation list to only consider the top k items
    top_k_rec = recommended[:k]
    
    # Use sets for O(1) lookups
    relevant_set = set(relevant)
    top_k_set = set(top_k_rec)
    
   
    hits = len(top_k_set.intersection(relevant_set))
    
    
    precision = hits / k if k > 0 else 0
    
    
    recall = hits / len(relevant) if len(relevant) > 0 else 0
    
    return [precision, recall]