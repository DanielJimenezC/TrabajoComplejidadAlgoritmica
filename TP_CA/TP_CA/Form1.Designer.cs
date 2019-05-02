namespace TP_CA
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.tb_01 = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.rb_01 = new System.Windows.Forms.RadioButton();
            this.rb_02 = new System.Windows.Forms.RadioButton();
            this.rb_03 = new System.Windows.Forms.RadioButton();
            this.tb_03 = new System.Windows.Forms.TextBox();
            this.tb_02 = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.b_recorrido = new System.Windows.Forms.Button();
            this.label5 = new System.Windows.Forms.Label();
            this.tb_04 = new System.Windows.Forms.TextBox();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(18, 30);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(99, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "Numero de Nodos: ";
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.tb_01);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(231, 70);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Generador de Grafo";
            // 
            // tb_01
            // 
            this.tb_01.Location = new System.Drawing.Point(123, 27);
            this.tb_01.Name = "tb_01";
            this.tb_01.Size = new System.Drawing.Size(83, 20);
            this.tb_01.TabIndex = 1;
            this.tb_01.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.tb_01.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this._KeyPress);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(18, 30);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(112, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "Seleccione Algoritmo: ";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.rb_03);
            this.groupBox2.Controls.Add(this.rb_02);
            this.groupBox2.Controls.Add(this.rb_01);
            this.groupBox2.Controls.Add(this.label2);
            this.groupBox2.Location = new System.Drawing.Point(249, 16);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(391, 66);
            this.groupBox2.TabIndex = 3;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Algoritmo de Recorrido";
            // 
            // rb_01
            // 
            this.rb_01.AutoSize = true;
            this.rb_01.Location = new System.Drawing.Point(136, 28);
            this.rb_01.Name = "rb_01";
            this.rb_01.Size = new System.Drawing.Size(77, 17);
            this.rb_01.TabIndex = 3;
            this.rb_01.TabStop = true;
            this.rb_01.Text = "Algoritmo 1";
            this.rb_01.UseVisualStyleBackColor = true;
            // 
            // rb_02
            // 
            this.rb_02.AutoSize = true;
            this.rb_02.Location = new System.Drawing.Point(219, 28);
            this.rb_02.Name = "rb_02";
            this.rb_02.Size = new System.Drawing.Size(77, 17);
            this.rb_02.TabIndex = 4;
            this.rb_02.TabStop = true;
            this.rb_02.Text = "Algoritmo 2";
            this.rb_02.UseVisualStyleBackColor = true;
            // 
            // rb_03
            // 
            this.rb_03.AutoSize = true;
            this.rb_03.Location = new System.Drawing.Point(302, 28);
            this.rb_03.Name = "rb_03";
            this.rb_03.Size = new System.Drawing.Size(77, 17);
            this.rb_03.TabIndex = 5;
            this.rb_03.TabStop = true;
            this.rb_03.Text = "Algoritmo 3";
            this.rb_03.UseVisualStyleBackColor = true;
            // 
            // tb_03
            // 
            this.tb_03.Location = new System.Drawing.Point(12, 321);
            this.tb_03.Multiline = true;
            this.tb_03.Name = "tb_03";
            this.tb_03.ReadOnly = true;
            this.tb_03.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tb_03.Size = new System.Drawing.Size(623, 66);
            this.tb_03.TabIndex = 4;
            // 
            // tb_02
            // 
            this.tb_02.Location = new System.Drawing.Point(12, 158);
            this.tb_02.Multiline = true;
            this.tb_02.Name = "tb_02";
            this.tb_02.ReadOnly = true;
            this.tb_02.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.tb_02.Size = new System.Drawing.Size(628, 120);
            this.tb_02.TabIndex = 5;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(12, 132);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(36, 13);
            this.label3.TabIndex = 6;
            this.label3.Text = "Grafo:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(9, 292);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(103, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "Recorrido de Grafo: ";
            // 
            // b_recorrido
            // 
            this.b_recorrido.Location = new System.Drawing.Point(481, 403);
            this.b_recorrido.Name = "b_recorrido";
            this.b_recorrido.Size = new System.Drawing.Size(154, 23);
            this.b_recorrido.TabIndex = 8;
            this.b_recorrido.Text = "Calcular Recorrido";
            this.b_recorrido.UseVisualStyleBackColor = true;
            this.b_recorrido.Click += new System.EventHandler(this.b_recorrido_Click);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(13, 100);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(91, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Nodo Inicial-Final:";
            // 
            // tb_04
            // 
            this.tb_04.Location = new System.Drawing.Point(110, 97);
            this.tb_04.Name = "tb_04";
            this.tb_04.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.tb_04.Size = new System.Drawing.Size(75, 20);
            this.tb_04.TabIndex = 10;
            this.tb_04.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
            this.tb_04.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this._KeyPress02);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(656, 446);
            this.Controls.Add(this.tb_04);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.b_recorrido);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.tb_02);
            this.Controls.Add(this.tb_03);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Recorrido de Grafo";
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.TextBox tb_01;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.RadioButton rb_03;
        private System.Windows.Forms.RadioButton rb_02;
        private System.Windows.Forms.RadioButton rb_01;
        private System.Windows.Forms.TextBox tb_03;
        private System.Windows.Forms.TextBox tb_02;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Button b_recorrido;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox tb_04;
    }
}

