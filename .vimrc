" Ensure vim-plug is installed
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
colorscheme desert

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
