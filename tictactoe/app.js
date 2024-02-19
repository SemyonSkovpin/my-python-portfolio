// helper functions
function indTo2D (ind, arrWidth)
{
    //When we want to numerate elements in 2D array we do like in writing: start on top line, go from left to right, go to line lower, repeat until end. 
    // it will take number of 2D array element and turn it into 2D coordinates
    // on the board from HTML document, numbers start from 0
    return [Math.floor((ind)/ arrWidth), (ind) % arrWidth]
}


function indTo1D (indArr, width)
{
    return indArr[0] * width + indArr[1]
}


// this function is from stackoverflow with slight change
function removeElementsByClass (className)
{
    const elements = document.getElementsByClassName (className);
    while (elements.length > 0)
    {
        elements[0].remove();
    }
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
// end of helper functions section


const boardObj = 
{
    // information, game logic is worked out separately in the boardObj
    // It does allow adding more that one winning row. The winCheck function will just choose first row in its order of precedence
    matrix :
    [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ],

    Xturn : true,

    makeTurn : function (cellCr)
    {
        // add x/o to matrix
        // the boardObj will just ignore function calls that would occupate cell that was alredy taken
        if (this.matrix[cellCr[0]][cellCr[1]] == '') 
        {
            if (this.Xturn)
            {
                this.matrix[cellCr[0]][cellCr[1]] = 'x'
            }
            else
            {
                this.matrix[cellCr[0]][cellCr[1]] = 'o'
            }
            this.Xturn = !this.Xturn
            console.log(this.matrix)
        }
    },

    winCheck : function (matrix)
    {
        /* 
        This function takes any 3x3 array with '', 'x', 'o'
        It then returns: null or [<'x' or 'o'>, <array with coordinates of winning cells>]
        */
    
        function isWinRow (row)
        {
            // get coordinates of the cell and its 2 neighbors 
            cell = matrix[row[0][0]][row[0][1]]
            n1 = matrix[row[1][0]][row[1][1]]
            n2 = matrix[row[2][0]][row[2][1]]

            if (cell == n1 && cell == n2 && cell != '')
            {
                return true
            }
            else 
            {
                return false
            }
        }

        const RowsToCheck = 
        [
            [[0,0], [1,0], [2,0]], // first collumn
            [[0,1], [1,1], [2,1]], // second collumn
            [[0,2], [1,2], [2,2]], // third collumn

            // rows down here
            [[0,0], [0,1], [0,2]],
            [[1,0], [1,1], [1,2]],
            [[2,0], [2,1], [2,2]],

            // diagonals
            [[0,0], [1,1], [2,2]],
            [[0,2], [1,1], [2,0]]
        ]

        for (const row of RowsToCheck)
        {
            if (isWinRow (row))
            {
                return [matrix[row[0][0]][row[0][1]], row]
            }
        }
        return null // if none of rows in loop is winning, return null
    },

    reset : function () 
    {
        this.matrix = 
        [
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ]
        this.Xturn = true
    }
}

function turnUpdate ()
{
    // This function wont add the most recent cell added, rather it will look at the whole boardObj.matrix and overwrite the board element accordingly. Erase all canvases with X/O in board element, add new from matrix. It will erase and rewrite all canvaces on board just to add one new 

    function buildX ()
    {
        // return canvas with X
        const X = document.createElement('canvas')
        X.classList.add('x')
        X.width = 100
        X.height = 100

        const ctx = X.getContext ('2d')
        ctx.beginPath()
        ctx.moveTo(0, 0)
        ctx.lineTo(100, 100)
        ctx.moveTo(100, 0)
        ctx.lineTo(0, 100)
        ctx.stroke()

        return X
    }

    function buildO ()
    {
        // return canvas with O
        const O = document.createElement('canvas')
        O.classList.add('o')
        O.width = 100
        O.height = 100

        const ctx = O.getContext ('2d')
        ctx.beginPath()
        ctx.arc(50, 50, 49, 0, 2 * Math.PI)
        ctx.stroke()
        return O
    }

    // erase all X/O canvaces
    removeElementsByClass('x')
    removeElementsByClass('o')

    // loop for matrix. Add X/O canvaces according to it
    for (let row = 0; row < boardObj.matrix.length; row++)
    {
        for (let col = 0; col < boardObj.matrix[row].length; col++)
        {
            if (boardObj.matrix[row][col] == 'x')
            {
                boardCells[indTo1D([row, col], 3)].appendChild(buildX())
            }
            else if (boardObj.matrix[row][col] == 'o')
            {
                boardCells[indTo1D([row, col], 3)].appendChild(buildO())
            }
        }
    }
}


// Now make turns happen when you tap on board DOM element (one that was writed with HTML)
const boardCells = document.getElementsByClassName ('boardCell')
for (let i = 0; i < boardCells.length; i++)
{
    boardCells[i].onclick = function () 
    {
        boardObj.makeTurn(indTo2D(i, 3))
        turnUpdate()
        if (boardObj.winCheck(boardObj.matrix))
        {
            setTimeout(function () { 

                alert (
`${boardObj.winCheck(boardObj.matrix)[0].repeat(30)}
${' '.repeat(19)}WINNER
${boardObj.winCheck(boardObj.matrix)[0].repeat(30)}`
                )

                boardObj.reset()
                turnUpdate()
            }, 0) 
        }

    }
}



