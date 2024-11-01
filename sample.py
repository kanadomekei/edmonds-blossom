from max_matching import Match
import networkx as nx
import matplotlib.pyplot as plt
import time

def visualize_matching(edges, num_nodes, matching):
    # グラフの作成
    G = nx.Graph()
    
    # ノードの追加
    G.add_nodes_from(range(num_nodes))
    
    # 全てのエッジを追加（重複を避けるため片方向のみ）
    unique_edges = [(i, j) for i, j in edges if i < j]
    G.add_edges_from(unique_edges)
    
    # マッチングされたエッジと通常のエッジで色分けする
    matched_edges = [(i, j) for i, j in matching]
    unmatched_edges = [e for e in unique_edges if e not in matched_edges and (e[1], e[0]) not in matched_edges]
    
    # グラフの描画
    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 10))
    
    # 通常のエッジを描画（灰色）
    nx.draw_networkx_edges(G, pos, edgelist=unmatched_edges, edge_color='gray')
    
    # マッチングされたエッジを描画（赤色、太線）
    nx.draw_networkx_edges(G, pos, edgelist=matched_edges, edge_color='red', width=2)
    
    # ノードを描画
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    
    # ノードのラベルを描画
    nx.draw_networkx_labels(G, pos)
    
    plt.title("Maximum Matching Result")
    plt.axis('off')
    plt.show()

def find_maximum_matching(edges, num_nodes):
    match = Match.from_edges(num_nodes, edges)
    match.maximum_matching()
    
    matching_result = []
    visited = set()
    for node in match.nodes:
        if node.mate and node not in visited:
            matching_result.append((node.index, node.mate.index))
            visited.add(node)
            visited.add(node.mate)
    
    return matching_result

if __name__ == "__main__":
    num_nodes = 10
    
    edges = [
        (0, 1), (1, 0),
        (2, 3), (3, 2),
        (4, 5), (5, 4),
        (6, 7), (7, 6),
        (1, 8), (8, 1),
        (1, 9), (9, 1),
        (3, 8), (8, 3),
        (3, 9), (9, 3),
        (5, 8), (8, 5),
        (5, 9), (9, 5),
        (7, 8), (8, 7),
        (7, 9), (9, 7),
        (3, 9), (9, 3),
    ]
    
    # 計測開始
    start_time = time.time()
    
    # 最大マッチングを計算
    matching = find_maximum_matching(edges, num_nodes)
    
    # 計測終了
    end_time = time.time()
    execution_time = end_time - start_time
    
    # 結果の表示
    print("Maximum Matching:")
    for edge in matching:
        print(f"Node {edge[0]} - Node {edge[1]}")
    
    print(f"\n実行時間: {execution_time:.6f} 秒")
    
    # マッチングされていない頂点の数を表示
    match = Match.from_edges(num_nodes, edges)
    unmatched = match.unmatched_nodes()
    print(f"\nNumber of unmatched nodes: {unmatched}")
    
    # グラフの可視化
    visualize_matching(edges, num_nodes, matching)