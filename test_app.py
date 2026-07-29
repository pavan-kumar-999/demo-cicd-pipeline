from app import main

def test_main_runs(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello" in captured.out