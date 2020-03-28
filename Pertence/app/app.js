var app = angular.module("app", []);
app.controller("AlunosController", function($scope) {
   
    //conjunto de alunos
    $scope.alunos = [];

   //Adiciona um aluno ao conjunto de alunos
   $scope.InserirAluno = (aluno) =>
   {
       if(aluno.nome){
        $scope.alunos.push(aluno);
        $scope.aluno = criarAluno();
       }
       else
        alert("É necessário digitar um nome!");
   };

   //Altera a aprovação do aluno pela tabela de alunos
   $scope.alterarAprovacao = (aluno) =>
   {
       //Existe a verificação se o aluno existe em alunos, 
       //caso sim o valor de aprovação é alterado pela função chamada pelo botão no html na tabela de alunos
        $scope.alunos.forEach(a => {
            if(a.nome==aluno.nome)
            {
                a.aprovado = !a.aprovado

                if(a.aprovado == false)
                    alert("Reprovado!")
                else
                    alert("Aprovado!")
            }
        });

   };

   //cria um novo aluno depois que um é adicionado ao conjunto de alunos
   function criarAluno() {
       return{
           nome:'',
           aprovado:true
       }
   }
   function inicio() {
       $scope.aluno = criarAluno();
   }
   //Com a lógica do angular no html foi feito a separação dos alunos aprovados e reprovados
   inicio();
});