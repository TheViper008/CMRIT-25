import java.util.*;

class graphD

{

	int n;

	int adj[][];

	int visited[];

	int d[];

	static final int infinity=999;

	public void create_graph()

	{

		Scanner sc= new Scanner(System.in);

		System.out.println("Enter the number of nodes in the graph");

		n=sc.nextInt();

		int i,j;

		adj=new int[n+1][n+1];

		System.out.println("Enter cost adjacency matrix for graph");

		System.out.println("If two nodes are not connected enter 999");

		for(i=1;i<n+1;i++)

			for(j=1;j<n+1;j++)

				adj[i][j]=sc.nextInt();

		visited=new int[n+1];

		d=new int[n+1];

	}

			public void find_path() 

			{

				int source,i,j;

				Scanner sc =new Scanner(System.in);

				for(i=0;i<n+1;i++)

				{

					visited[i]=0;

					d[i]=infinity;

				}

				System.out.println("Enter the index of the source code");

				source=sc.nextInt();

				visited[source]=1;

				d[source]=0;

				int u=source;

				int v,min_node;

				for(i=2;i<n+1;i++)

				{

					for(v=1;v<n+1;v++)

						if (visited[v]==0 && d[v]>d[u]+adj[u][v])

							d[v]=d[u]+adj[u][v];

					min_node=0;

					for(j=1;j<n+1;j++)

						if(visited[j]==0 && d[j]<d[min_node])

							min_node=j;

					if(d[min_node]<infinity)

						visited[min_node]=1;

					else break;

					u=min_node;

				}

				for(i=1;i<n+1;i++)

					System.out.println("Distance from source to " +i+ " is "+d[i]);

			}

}

public class shortdis{

	public static void main(String[] args)

	{

		graphD graph=new graphD();

		graph.create_graph();

		graph.find_path();

	}

}