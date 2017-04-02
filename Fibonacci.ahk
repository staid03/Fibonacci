#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance , Force

;Version	Date		Author		Comment
;	0.1		02-APR-17	Staid03		Initial

;Script Purpose: simple Fibonacci number generation up to limit

FormatTime , atime , , yyyyMMdd_HHmmss
outFile = Fibonacci_AHK_%atime%.txt
limit = 10000

main:
{
	GoSub , createFibonacci
	Run , %outFile%
}
Return

createFibonacci:
{
	x = 0
	y = 1
	FileAppend , %x%`n%y%`n , %outFile%
	Loop ,
	{
		IfGreater , z , %limit%
		Return
		z := x + y
		FileAppend , %z%`n , %outFile%
		x := y
		y := z
	}
}
Return
