from django.shortcuts import render
from board.models import Board
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    return render(request, "home.html")

def board(request):
    rsboard = Board.objects.all()

    return render(request, "board_list.html", {
        "rsboard": rsboard
    })

def board_write(request):
    return render(request, "board_write.html", )

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')
    else:
        return redirect('/board_writer')


def board_view(request):
    bno = request.GET['b_no']
    rsdetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        "rsdetail": rsdetail
    })

def board_edit(request):
    bno = request.GET['b_no']
    rsdetail = Board.objects.filter(b_no=bno)

    return render(request, "board_edit.html", {
        "rsdetail": rsdetail
    })


def board_update(request):
    bno = request.GET['b_no']
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    try:
        board = Board.objects.get(b_no=bno)
        if btitle != "":
            board.b_title = btitle
        if bnote != "":
            board.b_note = bnote
        if bwriter != "":
            board.b_writer = bwriter

        try:
            board.save()
            return redirect('/board')
        except ValueError:
            return HttpResponse({"success": False, "msg": "에러입니다."})

    except ObjectDoesNotExist:
        return HttpResponse({"success": False, "msg": "게시글 없음"})

def board_delete(request):
    bno = request.GET['b_no']
    rows = Board.objects.get(b_no=bno).delete()

    return redirect('/board')

