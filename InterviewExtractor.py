interviewers = ['Sean Hannity', 'Linda', 'Jim', 'Mark', 'Speaker 1']
interviewee = 'Donald Trump'

original_transcript_file = open('Corpuses/Interviews/Trump-Interview.txt', 'r')
transcript = original_transcript_file.readlines()
original_transcript_file.close()

extracted_transcript_file = open('Corpuses/Interviews/Trump-interview-extracted.txt', 'w')

keep_next_line = False
for single_line in transcript:
    keep_this_line = keep_next_line

    single_line_starts_with_interviewer = False
    for interviewer in interviewers:
        if single_line.startswith(interviewer):
            single_line_starts_with_interviewer = True
            keep_next_line = False

    if single_line.startswith(interviewee):
        keep_next_line = True

    if (keep_this_line is True) and (not single_line_starts_with_interviewer) and (not single_line.startswith(interviewee)):
        extracted_transcript_file.write(single_line)

extracted_transcript_file.close()
