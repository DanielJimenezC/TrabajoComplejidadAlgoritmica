using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TP_CA
{
    public partial class Form1 : Form
    {
        public Bitmap picture;

        public List<List<int>> Grafo;

        public static List<List<int>> GeneraG(int n)
        {
            List<List<int>> Grafo = new List<List<int>>();
            List<int> nodo;
            List<int> nodo_t;
            Random rdn = new Random();

            for (int i = 0; i < n; i++)
            {
                nodo_t = new List<int>();
                nodo = new List<int>();
                for (int j = 0; j < n; j++)
                {
                    if (i != j)
                    {
                        nodo_t.Add(j);
                    }
                }
                while (nodo_t.Count() > 0)
                {
                    int val = rdn.Next(0, nodo_t.Count());
                    nodo.Add(nodo_t[val]);
                    nodo_t.RemoveAt(val);
                }
                Grafo.Add(nodo);
            }
            return Grafo;
        }

        public static bool FoundT(List<bool> L)
        {
            if (L.Contains(false))
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        public static void Llenar(ref List<bool> L, int n)
        {
            for (int i = 0; i < n; i++)
            {
                L.Add(false);
            }
        }

        public List<List<int>> resultString = new List<List<int>>();

        public void BackTracking(List<List<int>> G,  int v, List<bool> visited, int vp, List<int> orden)
        {
            List<int> opciones = new List<int>();
            visited[v] = true;
            orden.Add(v);
            var auxVisited = visited;
            var auxOrden = orden;
            foreach( var u in G[v])
            {
                if(visited[u] == false)
                {
                    opciones.Add(u);
                }
            }
            foreach(var u in opciones)
            {
                BackTracking(G, u, visited, vp, orden);
                visited = auxVisited;
                orden = auxOrden;
            }
            if( visited.Where(x=>x == true).Count() == G.Count() && opciones.Count() == 0 && G[v].Contains(vp))
            {
                resultString.Add(orden);
            }
        }

        public static string FoundWay(List<List<int>> G, int s)
        {
            int n = G.Count();
            //Stack<int> Rest = new Stack<int>();
            string Resultado = "";
            List<bool> visited = new List<bool>();
            List<bool> queued = new List<bool>();
            List<int> reverse = new List<int>();
            Stack<int> q = new Stack<int>();
            Llenar(ref visited, n);
            Llenar(ref queued, n);
            queued[s] = true;
            q.Push(s);
            int temp = 1;
            int u = 0;
            while (q.Count() > 0)
            {
                u = q.Pop();
                Resultado += "paso " + temp + " --->\t" + u + "{0}";
                //Rest.Push(u);
                temp += 1;
                if (!visited[u])
                {
                    visited[u] = true;
                    reverse = G[u];
                    reverse.Reverse();
                    foreach (int v in reverse)
                    {
                        if (FoundT(visited) == true && v == s)
                        {
                            q.Push(v);
                            break;
                        }
                        else if (!queued[v])
                        {
                            queued[v] = true;
                            q.Push(v);
                        }
                    }
                    reverse.Clear();
                }
            }
            return Resultado;
        }

        private static void GenerarTXT(string texto)
        {
            TextWriter tw = new StreamWriter("graph.txt");
            tw.WriteLine(texto);
            tw.Close();
        }

        private static void GenerarJPG(string fileName)
        {
            try
            {
                string executable = @"C:\Program Files (x86)\Graphviz2.38\bin\dot.exe";
                string output = @"D:\TP\TP_CA\TP_CA\bin\Debug\graph";
                File.WriteAllText(output, fileName);

                Process proc = new Process();

                proc.StartInfo.RedirectStandardOutput = true;
                proc.StartInfo.UseShellExecute = false;
                proc.StartInfo.CreateNoWindow = true;

                proc.StartInfo.FileName = executable;
                proc.StartInfo.Arguments = string.Format(@"{0} -Tjpg -O", output);

                proc.Start();
                proc.WaitForExit();

            }
            catch (Exception x)
            {
                Console.WriteLine(x.ToString());
            }
        }

       /* private static List<int> BFS(List<List<int>> tree, List<int> level)
        {
            List<int> bfs_list = new List<int>();
            
            if (level.Count() > 0)
            {
                bfs_list.AddRange(level);
                List<int> sub_level = new List<int>();

                foreach(var v in level)
                {
                    if (!tree.Contains(v))
                    {
                        continue;
                    }
                }
            }
        }*/

        public Form1()
        {
            InitializeComponent();
            rb_01.Checked = true;
        }

        private void b_recorrido_Click(object sender, EventArgs e)
        {
            StringBuilder b = new StringBuilder();
            b.Append("digraph G {" + Environment.NewLine);

            if(tb_01.Text == "" || int.Parse(tb_01.Text) <= 2)
            {
                MessageBox.Show("Ingrese un numero de nodos mayor o igual a 3", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else if(tb_04.Text == "")
            {
                MessageBox.Show("Ingrese Nodo Inicial-Final", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                int n = int.Parse(tb_01.Text);
                int _ini_ = int.Parse(tb_04.Text);
                string texto = "";
                string Result;
                string GrafoText;

                Grafo = GeneraG(n);

                if(_ini_ < Grafo.Count())
                {
                   
                    for (int i = 0; i < Grafo.Count(); i++)
                    {
                        texto += "Nodo " + i + ": \t";
                        for (int j = 0; j < Grafo[i].Count(); j++)
                        {
                            b.AppendFormat("{0}->{1}{2}", string.Format("\"{0}\"", i), string.Format("\"{0}\"", Grafo[i][j]), Environment.NewLine);
                            texto += Grafo[i][j] + "\t";
                        }
                        texto += "{0}{0}";
                    }

                    b.Append("}");

                    GenerarTXT(b.ToString());

                    GenerarJPG(b.ToString());

                    //Process.Start("graph.jpg");

                    GrafoText = string.Format(texto, Environment.NewLine);
                    tb_02.Text = GrafoText;

                    if (rb_01.Checked)
                    {
                        Result = string.Format(FoundWay(Grafo, _ini_), Environment.NewLine);
                        tb_03.Text = Result;
                        MessageBox.Show("Se encontró el camino con algoritmo 1","Encontrado", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    else if (rb_02.Checked)
                    {
                        List<bool> visited = new List<bool>();
                        Llenar(ref visited, n);
                        List<int> orden = new List<int>();

                        BackTracking(Grafo,_ini_,visited,_ini_,orden);

                        List<string> lista = new List<string>();
                        string mensaje = string.Empty;
                        int i = 0;

                        foreach (var j in resultString)
                        {
                            mensaje += "opcion " + i + " : ";
                            foreach(var z in j)
                            {
                                if (z != j.Last())
                                {
                                    mensaje += z + " -> ";
                                }
                                else
                                {
                                    mensaje += z;
                                }
                            }
                            mensaje += "\t";
                            i++;
                        }

                        tb_03.Text = mensaje;

                        MessageBox.Show("algo 02", "Encontrado", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                    else if (rb_03.Checked)
                    {
                        MessageBox.Show("algo 03", "Encontrado", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                else
                {
                    MessageBox.Show("El Nodo "+ _ini_ + " debe estar dentro del Grafo","Fuera de Rango", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }

        }

        private void _KeyPress(object sender, KeyPressEventArgs e)
        {
            if (Char.IsDigit(e.KeyChar))
            {
                e.Handled = false;
            } else if(Char.IsControl(e.KeyChar)) 
            {
                e.Handled = false;
            } else
            {
                e.Handled = true;
            }
        }

        private void _KeyPress02(object sender, KeyPressEventArgs e)
        {
            if (Char.IsDigit(e.KeyChar))
            {
                e.Handled = false;
            }
            else if (Char.IsControl(e.KeyChar))
            {
                e.Handled = false;
            }
            else
            {
                e.Handled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Process.Start("graph.jpg");
        }

    }
}
