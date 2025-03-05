"Ensure vim-plug is installed
if empty(glob('~/.vim/autoload/plug.vim'))
	  silent !curl -fLo ~/.vim/autoload/plug.vim --create-dirs
	        \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
	    autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.vim/plugged')

" ========== Python IDE Enhancements ==========
Plug 'neoclide/coc.nvim', {'branch': 'release'}  " Auto-completion & LSP
Plug 'dense-analysis/ale'  " Linting & Formatting
Plug 'psf/black', {'branch': 'main'}  " Auto-format with Black
Plug 'vim-python/python-syntax'  " Improved Python syntax highlighting
Plug 'vim-scripts/indentpython.vim'  " Better indentation
Plug 'puremourning/vimspector'  " Debugging

" ========== General Productivity ==========
Plug 'preservim/nerdtree'  " File Explorer
Plug 'Xuyuanp/nerdtree-git-plugin'  " Git integration for NERDTree
Plug 'ctrlpvim/ctrlp.vim'  " Fuzzy file finder
Plug 'vim-airline/vim-airline'  " Status bar
Plug 'vim-airline/vim-airline-themes'  " Themes for status bar
Plug 'tpope/vim-fugitive'  " Git integration
Plug 'jiangmiao/auto-pairs'  " Auto-closing brackets
Plug 'tpope/vim-commentary'  " Quick comments
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }  " Fast fuzzy finder
Plug 'voldikss/vim-floaterm'
Plug 'puremourning/vimspector'
Plug 'tomasiser/vim-code-dark'

call plug#end()

" ========== Editor Settings ==========
 syntax on
 set number
 set relativenumber
 set tabstop=4
 set shiftwidth=4
 set expandtab
 set autoindent
 set smartindent
 set encoding=utf-8
 set fileencoding=utf-8
 set cursorline
 set scrolloff=8
 set updatetime=300
 set signcolumn=yes
 set clipboard=unnamedplus
 set background=dark
 colorscheme codedark
let mapleader=","

" ========== Key Mappings ==========
nnoremap <C-n> :NERDTreeToggle<CR>  " Toggle file explorer
nnoremap <C-p> :CtrlP<CR>  " Fuzzy file search
nnoremap <Leader>f :Autoformat<CR>  " Format file with Black

" ========== Auto-completion & LSP (CoC.nvim) ==========
let g:coc_global_extensions = ['coc-pyright', 'coc-json', 'coc-git']

" Enable linting with flake8
let g:ale_linters = { 'python': ['flake8'] }
let g:ale_fixers = { 'python': ['black'] }
let g:ale_python_flake8_executable = 'flake8'
let g:ale_python_black_executable = 'black'
let g:ale_fix_on_save = 1

" ========== Debugging with Vimspector ==========
let g:vimspector_enable_mappings = 'HUMAN'
nmap <F5> <Plug>VimspectorContinue
nmap <F10> <Plug>VimspectorStepOver
nmap <F11> <Plug>VimspectorStepInto
nmap <F12> <Plug>VimspectorStepOut

" ========== Auto-format on Save ==========
autocmd BufWritePre *.py execute ':Black'





" ================================
 " 🚀 Vim IDE Shortcuts with Comma (,) as Leader
 " ================================

 " Set Leader Key to Comma
 let mapleader = ","

 " 🌲 NERDTree Shortcuts
 nnoremap <leader>e :NERDTreeToggle<CR>      " Toggle NERDTree
 nnoremap <leader>r :NERDTreeRefreshRoot<CR> " Refresh NERDTree

" 🖥️ Open Terminal in a Split
" nnoremap <leader>t :split | terminal<CR>  " Open terminal in horizontal split
" nnoremap <leader>vt :vsplit | terminal<CR>  " Open terminal in vertical split

" 🎯 Running Code (Python, C++, etc.)
nnoremap <leader>r :w<CR>:!python3 %<CR>  " Run Python
nnoremap <leader>c :w<CR>:!gcc -o %:r % && ./%:r<CR>  " Compile & Run C (for C programs)
nnoremap <leader>cpp :w<CR>:!g++ -o %:r % && ./%:r<CR>  " Compile & Run C++

" 🐞 Debugging with Vimspector
nnoremap <leader>db :call vimspector#Launch()<CR>  " Start Debugging
nnoremap <leader>dx :call vimspector#Reset()<CR>  " Stop Debugging
nnoremap <leader>bp :call vimspector#ToggleBreakpoint()<CR>  " Toggle Breakpoint

" 📂 Buffer Navigation
nnoremap <leader>bn :bn<CR>   " Next buffer
nnoremap <leader>bp :bp<CR>   " Previous buffer
nnoremap <leader>bd :bd<CR>   " Close current buffer

" 🖥️ Toggle Floating Terminal (Using vim-floaterm)
nnoremap <leader>ft :FloatermToggle<CR>
tnoremap <Esc> <C-\><C-n>:FloatermToggle<CR>

" 🔍 Quick Search & Replace
nnoremap <leader>sw :%s//g<Left><Left>  " Search & Replace

" 💾 Save and Quit
nnoremap <leader>w :w<CR>
nnoremap <leader>q :q<CR>
nnoremap <leader>x :x<CR>

" 🚀 Quick Access to Plugins
nnoremap <leader>pi :PlugInstall<CR>   " Install Plugins
nnoremap <leader>pu :PlugUpdate<CR>    " Update Plugins
nnoremap <leader>pc :PlugClean<CR>     " Clean Unused Plugins

" ================================
" 🚀 Window Navigation Remap
" ================================
nnoremap <C-j> <C-w>j   " Move to window below
nnoremap <C-k> <C-w>k   " Move to window above
nnoremap <C-h> <C-w>h   " Move to window left
nnoremap <C-l> <C-w>l   " Move to window right

