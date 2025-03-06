def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)
if __name__ == "__main__":
    candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
    # Write loop to find the ideal tree size from candidate_max_leaf_nodes
    _
    best_mae = float("inf")
    best_tree_size = None
    for value in candidate_max_leaf_nodes:
    # Store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
        my_mae  = get_mae(value, train_X, val_X, train_y, val_y)
        if my_mae < best_mae: 
            best_mae = my_mae
            best_tree_size = value 
        
    # Check your answer
    final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state=0)

    # fit the final model and uncomment the next two lines
    final_model.fit(X, y)