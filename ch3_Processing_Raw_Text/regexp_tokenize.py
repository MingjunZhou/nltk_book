import nltk


text = 'That U.S.A. poster-print costs $12.40...'
pattern = r'''(?x)                  # set flag to allow verbose regexps
              ([A-Z]\.)+            # abbreviations, e.g. U.S.A.
              | \w+(-\w+)*          # words with optional internal hyphens
              | \$?\d+(\.\d+)?%?    # currently and percentages, e.g. $12.40, 82%
              | \.\.\.              # ellipsis
              | [][.,;"'?():-_`]    # these are separate tokens
           '''
print nltk.regexp_tokenize(text, pattern)
