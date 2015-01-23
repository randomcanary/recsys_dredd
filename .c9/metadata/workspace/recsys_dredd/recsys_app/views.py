{"filter":false,"title":"views.py","tooltip":"/recsys_dredd/recsys_app/views.py","undoManager":{"mark":52,"position":52,"stack":[[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["","# Create your views here.",""]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":14,"column":49},"action":"insert","lines":["from django.http import HttpResponse","from django.template import RequestContext, loader","","from polls.models import Question","","","def index(request):","    latest_question_list = Question.objects.order_by('-pub_date')[:5]","    template = loader.get_template('polls/index.html')","    context = RequestContext(request, {","        'latest_question_list': latest_question_list,","    })","    return HttpResponse(template.render(context))"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":41},"end":{"row":10,"column":42},"action":"remove","lines":["/"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":40},"end":{"row":10,"column":41},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":39},"end":{"row":10,"column":40},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":38},"end":{"row":10,"column":39},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":37},"end":{"row":10,"column":38},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":36},"end":{"row":10,"column":37},"action":"remove","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":3},"end":{"row":9,"column":69},"action":"remove","lines":[" latest_question_list = Question.objects.order_by('-pub_date')[:5]"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":2},"end":{"row":9,"column":3},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":1},"end":{"row":9,"column":2},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":0},"end":{"row":9,"column":1},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":19},"end":{"row":9,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":0},"end":{"row":5,"column":33},"action":"remove","lines":["","from polls.models import Question"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":50},"end":{"row":4,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":8},"end":{"row":9,"column":9},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"insert","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":["3"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":54},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":48},"end":{"row":8,"column":0},"action":"insert","lines":["",""]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["C"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["O"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["T"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["X"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["T"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["T"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["X"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["E"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["T"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["N"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["O"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["C"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["c"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["="]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["\""]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["{"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["}"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":47},"end":{"row":11,"column":47},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1421881545995,"hash":"ec24b6fe294e8d6f2b47bde36adb26ccd93b6bcc"}