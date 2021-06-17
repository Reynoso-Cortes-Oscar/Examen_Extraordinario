from sklearn import tree
import webbrowser
datos = []
with open ('Registro.csv','r') as archivo:
    lineas = archivo.read().splitlines()
    lineas.pop(0)
    for i in lineas:
        linea = i.split(',')
        datos.append([str(linea[0]), str(linea[1]), str(linea[2]), str(linea[3]), str(linea[4]), str(linea[5]), str(linea[6]), str(linea[7]), str(linea[8]), str(linea[9]), str(linea[10]), str(linea[11]), str(linea[12]), str(linea[13]), str(linea[14]), str(linea[15])])

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
ii = []
j = []
k = []
l = []
m = []
n = []
o = []
p = []

for elem in sorted(datos):
    a.append(elem[0])
    b.append(elem[1])
    c.append(elem[2])
    d.append(elem[3])
    e.append(elem[4])
    f.append(elem[5])
    g.append(elem[6])
    h.append(elem[7])
    ii.append(elem[8])
    j.append(elem[9])
    k.append(elem[10])
    l.append(elem[11])
    m.append(elem[12])
    n.append(elem[13])
    o.append(elem[14])
    p.append(elem[15])

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(ii)
print(j)
print(k)
print(l)
print(m)
print(n)
print(o)
print(p)

respuestas=[]

features = [["17","0","1","2","4","9","9","9","8","9","1","1","1","1","1"],["17","0","1","1","4","7","7","8","7","6","1","1","1","1","2"],["18","1","3","3","2","7","8","9","10","9","2","1","1","1","2"],["18","1","2","4","2","9","9","9","10","10","1","1","1","1","1"],["17","0","3","3","4","6","9","7","6","9","1","2","2","1","2"],["17","0","2","1","4","9","9","9","8","8","1","1","1","1","1"],["18","1","1","3","4","8","8","8","8","8","1","1","1","1","1"]]
labels=["1","0","0","1","0","1","1"]
classifier = tree.DecisionTreeClassifier()
classifier.fit(features,labels)
for i in range(len(a)):
    res = classifier.predict([[b[i],c[i],d[i],e[i],f[i],g[i],h[i],ii[i],j[i],k[i],l[i],m[i],n[i],o[i],p[i]]])
    respuestas.append(res)
print(respuestas)
datosStrTree="["
for i in range(len(respuestas)):
    if(i==len(respuestas)-1):
        datosStrTree=datosStrTree+str(respuestas[i])+"]"
    elif(i<len(respuestas)):
        datosStrTree=datosStrTree+str(respuestas[i])+','
print("cadena")
datosStrTreeFinal=datosStrTree.replace("[", "")
datosStrTreeFinal=datosStrTreeFinal.replace("]", "")
print(datosStrTreeFinal)
ceros = datosStrTreeFinal.count("0")
unos = datosStrTreeFinal.count("1")
print(ceros)
print(unos)

fig = open('Py.html', 'w')
mensaje = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/Py.css">
    <script src="Chart.js"></script>
    <title>EXAMEN EXTRAORDINARIO</title>
</head>
<body>
        <center>
            <div>
                <a href="Algo.html"><img src="al.png"width="13%"></a>
                <a href="Py.html"><img src="py.png"width="13%"></a>
                <a href="Index.html"><img src="pag.png"width="13%"></a>
            </div>
            <br>
            <div style="width:40%;">
                <canvas id="GraficaPY" width="400" height="300"></canvas>
            <p style = "font-family:courier,arial,helvetica;">Despues de haber analizado de manera detenida la informacion que recopilamos de nuestras encuestas decidimos emplear los arboles de regresion
            para predecir si un alumno aprobara la materia de probabilidad y estadistica tomando como base las demas respuestas que este proporciono en la encuesta
            </p>
            </div>
        </center>
        
</body>
<script>
    let Canvas=document.getElementById("GraficaPY").getContext("2d");
	var chart = new Chart(GraficaPY,{
		type:"bar",
		data:{
			labels:"""+"['Aprobatoria','Reprobatoria']"+""",
			datasets:[{
				label:"Prediccion de Personas que pasaran la materia de PyE",
				backgroundColor:"rgb(234,214,55)",
				borderColor:"rgb(255,255,255)",
                fill:true,
				data:["""+str(unos)+""","""+str(ceros)+"""]
                }]
		}
	})





</script>
</html>
"""
fig.write(mensaje)
fig.close()
webbrowser.open_new_tab('Py.html')









inde = open('Index.html', 'w')
mensajeIndex = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/Index.css">
    <script src="Chart.js"></script>
    <title>EXAMEN EXTRAORDINARIO</title>
</head>
<body>
        <center>
            <div>
                <a href="Algo.html"><img src="al.png"width="13%"></a>
                <a href="Py.html"><img src="py.png"width="13%"></a>
                <a href="Index.html"><img src="pag.png"width="13%"></a>
            </div>
            <br>
            <div id = "general">
                <div style="width:25%;" id="Preguntas1">
                    <canvas id="Pregunta1" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas2">
                    <canvas id="Pregunta2" width="400" height="300"></canvas>
                </div>
                
            </div>
            <div id="general2">
                <div style="width:25%;" id="Preguntas3">
                    <canvas id="Pregunta3" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas4">
                    <canvas id="Pregunta4" width="400" height="300"></canvas>
                </div>
            </div>
            <div id="general3">
                <div style="width:25%;" id="Preguntas5">
                    <canvas id="Pregunta5" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas6">
                    <canvas id="Pregunta6" width="400" height="300"></canvas>
                </div>
            </div>
            <div id="general4">
                <div style="width:25%;" id="Preguntas7">
                    <canvas id="Pregunta7" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas8">
                    <canvas id="Pregunta8" width="400" height="300"></canvas>
                </div>
            </div>
            <div id="general5">
                <div style="width:25%;" id="Preguntas9">
                    <canvas id="Pregunta9" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas10">
                    <canvas id="Pregunta10" width="400" height="300"></canvas>
                </div>
            </div>
            <div id="general6">
                <div style="width:25%;" id="Preguntas11">
                    <canvas id="Pregunta11" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas12">
                    <canvas id="Pregunta12" width="400" height="300"></canvas>
                </div>
            </div>
            <div id="general7">
                <div style="width:25%;" id="Preguntas13">
                    <canvas id="Pregunta13" width="400" height="300"></canvas>
                </div>
                <div style="width:25%;" id="Preguntas14">
                    <canvas id="Pregunta14" width="400" height="300"></canvas>
                </div>
            </div>
            <div id="general8">
                <div style="width:25%;" id="Preguntas15">
                    <canvas id="Pregunta15" width="400" height="300"></canvas>
                </div>
            </div>
        </center>
        
</body>
<script>
    let miCanvas=document.getElementById("Pregunta1").getContext("2d");
	var chart = new Chart(miCanvas,{
		type:"bar",
		data:{
			labels:"""+"['15','16','17','18']"+""",
			datasets:[{
				label:"Edad",
				backgroundColor: [
                  'rgba(255, 99, 132, 0.2)',
                  'rgba(255, 159, 64, 0.2)',
                  'rgba(255, 205, 86, 0.2)',
                  'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                  'rgb(255, 99, 132)',
                  'rgb(255, 159, 64)',
                  'rgb(255, 205, 86)',
                  'rgb(75, 192, 192)'
                ],
                fill:true,
				data:["""+str(b.count("15"))+""","""+str(b.count("16"))+""","""+str(b.count("17"))+""","""+str(b.count("18"))+"""]
                }]
		}
	})
    
let miCanvas2=document.getElementById("Pregunta2").getContext("2d");
	var chart = new Chart(miCanvas2,{
		type:"bar",
		data:{
			labels:"""+"['Masculino','Femenino']"+""",
			datasets:[{
				label:"Sexo",
				backgroundColor: [
                  'rgba(153, 102, 255, 0.2)',
                  'rgba(201, 203, 207, 0.2)'
                ],
                borderColor: [
                  'rgb(153, 102, 255)',
                  'rgb(201, 203, 207)'
                ],
                fill:true,
				data:["""+str(c.count("0"))+""","""+str(c.count("1"))+"""]
                }]
		}
	})
let miCanvas3=document.getElementById("Pregunta3").getContext("2d");
	var chart = new Chart(miCanvas3,{
		type:"bar",
		data:{
			labels:"""+"['Kinestesico','Visual','Auditivo']"+""",
			datasets:[{
				label:"Tipo de aprendizaje",
				backgroundColor: [
                    'rgba(54, 162, 235, 0.2)',
                  'rgba(105, 23, 20, 0.2)',
                  'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                'rgb(54, 162, 235)',
                  'rgb(153, 102, 255)',
                  'rgb(201, 203, 207)'
                ],
                fill:true,
				data:["""+str(d.count("1"))+""","""+str(d.count("2"))+""","""+str(d.count("3"))+"""]
                }]
		}
	})
let miCanvas4=document.getElementById("Pregunta4").getContext("2d");
	var chart = new Chart(miCanvas4,{
		type:"bar",
		data:{
			labels:"""+"['1','2','3','4']"+""",
			datasets:[{
				label:"Horas semanales estudio",
				backgroundColor: [
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(e.count("1"))+""","""+str(e.count("2"))+""","""+str(e.count("3"))+""","""+str(e.count("4"))+"""]
                }]
		}
	})
let miCanvas5=document.getElementById("Pregunta5").getContext("2d");
	var chart = new Chart(miCanvas5,{
		type:"bar",
		data:{
			labels:"""+"['1','2','3','4']"+""",
			datasets:[{
				label:"Horas semanales ocio",
				backgroundColor: [
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(f.count("1"))+""","""+str(f.count("2"))+""","""+str(f.count("3"))+""","""+str(f.count("4"))+"""]
                }]
		}
	})
let miCanvas6=document.getElementById("Pregunta6").getContext("2d");
	var chart = new Chart(miCanvas6,{
		type:"bar",
		data:{
			labels:"""+"['6','7','8','9','10']"+""",
			datasets:[{
				label:"Algebra",
				backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(g.count("6"))+""","""+str(g.count("7"))+""","""+str(g.count("8"))+""","""+str(g.count("9"))+""","""+str(g.count("10"))+"""]
                }]
		}
	})
let miCanvas7=document.getElementById("Pregunta7").getContext("2d");
	var chart = new Chart(miCanvas7,{
		type:"bar",
		data:{
			labels:"""+"['6','7','8','9','10']"+""",
			datasets:[{
				label:"Trigonometria",
				backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(h.count("6"))+""","""+str(h.count("7"))+""","""+str(h.count("8"))+""","""+str(h.count("9"))+""","""+str(h.count("10"))+"""]
                }]
		}
	})
let miCanvas8=document.getElementById("Pregunta8").getContext("2d");
	var chart = new Chart(miCanvas8,{
		type:"bar",
		data:{
			labels:"""+"['6','7','8','9','10']"+""",
			datasets:[{
				label:"Analitica",
				backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(ii.count("6"))+""","""+str(ii.count("7"))+""","""+str(ii.count("8"))+""","""+str(ii.count("9"))+""","""+str(ii.count("10"))+"""]
                }]
		}
	})
let miCanvas9=document.getElementById("Pregunta9").getContext("2d");
	var chart = new Chart(miCanvas9,{
		type:"bar",
		data:{
			labels:"""+"['6','7','8','9','10']"+""",
			datasets:[{
				label:"Diferencial",
				backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(j.count("6"))+""","""+str(j.count("7"))+""","""+str(j.count("8"))+""","""+str(j.count("9"))+""","""+str(j.count("10"))+"""]
                }]
		}
	})
let miCanvas10=document.getElementById("Pregunta10").getContext("2d");
	var chart = new Chart(miCanvas10,{
		type:"bar",
		data:{
			labels:"""+"['6','7','8','9','10']"+""",
			datasets:[{
				label:"Integral",
				backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                      'rgba(255, 205, 86, 0.2)',
                      'rgba(75, 192, 192, 0.2)',
                      'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)'
                ],
                fill:true,
				data:["""+str(k.count("6"))+""","""+str(k.count("7"))+""","""+str(k.count("8"))+""","""+str(k.count("9"))+""","""+str(k.count("10"))+"""]
                }]
		}
	})
let miCanvas11=document.getElementById("Pregunta11").getContext("2d");
	var chart = new Chart(miCanvas11,{
		type:"bar",
		data:{
			labels:"""+"['Primera Vez','Recurse']"+""",
			datasets:[{
				label:"Algebra",
				backgroundColor: [
                    'rgba(191, 49, 0, 0.4)',
                    'rgba(65, 103, 136, 0.2)'
                ],
                borderColor: [
                'rgb(191, 49, 0)',
                'rgb(65, 103, 136)'
                ],
                fill:true,
				data:["""+str(l.count("1"))+""","""+str(l.count("2"))+"""]
                }]
		}
	})
let miCanvas12=document.getElementById("Pregunta12").getContext("2d");
	var chart = new Chart(miCanvas12,{
		type:"bar",
		data:{
			labels:"""+"['Primera Vez','Recurse']"+""",
			datasets:[{
				label:"Trigo",
				backgroundColor: [
                    'rgba(191, 49, 0, 0.4)',
                    'rgba(65, 103, 136, 0.2)'
                ],
                borderColor: [
                'rgb(191, 49, 0)',
                'rgb(65, 103, 136)'
                ],
                fill:true,
				data:["""+str(m.count("1"))+""","""+str(m.count("2"))+"""]
                }]
		}
	})
let miCanvas13=document.getElementById("Pregunta13").getContext("2d");
	var chart = new Chart(miCanvas13,{
		type:"bar",
		data:{
			labels:"""+"['Primera Vez','Recurse']"+""",
			datasets:[{
				label:"Analitica",
				backgroundColor: [
                    'rgba(191, 49, 0, 0.4)',
                    'rgba(65, 103, 136, 0.2)'
                ],
                borderColor: [
                'rgb(191, 49, 0)',
                'rgb(65, 103, 136)'
                ],
                fill:true,
				data:["""+str(n.count("1"))+""","""+str(n.count("2"))+"""]
                }]
		}
	})
let miCanvas14=document.getElementById("Pregunta14").getContext("2d");
	var chart = new Chart(miCanvas14,{
		type:"bar",
		data:{
			labels:"""+"['Primera Vez','Recurse']"+""",
			datasets:[{
				label:"Diferencial",
				backgroundColor: [
                    'rgba(191, 49, 0, 0.4)',
                    'rgba(65, 103, 136, 0.2)'
                ],
                borderColor: [
                'rgb(191, 49, 0)',
                'rgb(65, 103, 136)'
                ],
                fill:true,
				data:["""+str(o.count("1"))+""","""+str(o.count("2"))+"""]
                }]
		}
	})
let miCanvas15=document.getElementById("Pregunta15").getContext("2d");
	var chart = new Chart(miCanvas15,{
		type:"bar",
		data:{
			labels:"""+"['Primera Vez','Recurse']"+""",
			datasets:[{
				label:"Integral",
				backgroundColor: [
                    'rgba(191, 49, 0, 0.4)',
                    'rgba(65, 103, 136, 0.2)'
                ],
                borderColor: [
                'rgb(191, 49, 0)',
                'rgb(65, 103, 136)'
                ],
                fill:true,
				data:["""+str(p.count("1"))+""","""+str(p.count("2"))+"""]
                }]
		}
	})
</script>
</html>
"""
inde.write(mensajeIndex)
inde.close()

